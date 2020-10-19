#!/usr/bin/env python3
import rospy, os, math
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32,Float32MultiArray
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,Polygon
import numpy as np

#Clase para manejar el nodo Soccer Futbol Player

class soccerRobot():


    def __init__(self,K):
        """Metodo que inicializa las variables del robot

        Args:
            K ([Integer]): Constantes de control, Kx,Ky,Ktheta, tiene que ser de tamaño 3 el arrego
        """
        #Nombre del nodo
        self.name = 'soccer_futbol_player'
        
        #Variable que indica si el robot ya acabo su recorrido
        self.end=False
        
        #Variable que representa al eje de la grafica, su valor se da en initPlot()
        self.ax = None
        
        #Listado de topicos
        self.topicos = ['/kickpower','/robot_move_vel','/robot_Position','/ball_Position']
        
        #Path para guardar la grafica
        self.path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'results/trayectoria_pelota.png')
       
        #Atributo que guarda la posición de la pelota
        self.ballPos = None
        
        #Lista para guardar las posiciones del robot, contiene listas con el siguiente formato:
        #[posX,posY,orientacion]
        self.robotPos=[]
        
        #Variable que representa en que cancha va a hacer gol el robot, False si es izquierda, True si es derecha.
        #Se inicializa como None
        self.cancha=None
        
        #Lista con las posiciones de las canchas, estas son P(x,y):
        #P(-6,0), P(6,0) 
        self.posGoal=[[-6,0],[6,0]]
        
        #Constantes para control del robot 
        assert (len(K)==3),"El arreglo de constantes de control no posee exactamente 3 valores"
        self.K = K
        
        #Arreglo con la ruta a seguir del robot, contiene posiciones [x,y]
        self.route=[]
        
        #Arreglo de publishers
        self.pub=[
            rospy.Publisher(self.topicos[0],Float32,queue_size=10),
            rospy.Publisher(self.topicos[1],Twist,queue_size=10)
        ]
        
        #Subscriptores
        rospy.Subscriber(self.topicos[2],Twist,self.posCallBack)
        rospy.Subscriber(self.topicos[3],Float32MultiArray,self.ballCallBack)
        return
    
    
    def __call__(self):
        """Función que inicializa el funcionamento del nodo
        """
        
        #Se inicializa la grafica
        plt.ion()
        plt.show()
        self.ax = self.initPlot()
        plt.draw()
        plt.pause(1)
        
        print("Se va a iniciar el nodo")  #Notificación a consola
        
        rospy.init_node(self.name,anonymous=True)
        self.rate= rospy.Rate(10)
        rospy.sleep(1)  #Se duerme 1 segundo para asegurar que la grafica va a estar inicialziada antes que comience el nodo de ros
       
        
        
        #En este loop se ejecuta el algoritmo de control
        while not (rospy.is_shutdown() or self.end):
            self.control()
            plt.draw()
            plt.pause(1/100)    #Se actualiza la grafica
            self.rate.sleep()
            
        print("Termino la ejecución, se va a guardar la grafica")   #Notificación a consola
        self.pub[1].publish(Twist())
        plt.savefig(self.path)  #Se guarda la grafica
        plt.close()
        
        
    
    def initPlot(self):
        """Función encargada de inicializar la grafica donde se va guardar el recorrido del robot
        """
        plt.title("Ubicación del robot")    #Titulo de la grafica
        plt.xlim(-7,7)  #Limite en X
        plt.ylim(-5.5,5.5)  #Limite en Y
        rect = Rectangle((-6,-4.5),6*2,4.5*2,linewidth=2,edgecolor='black',facecolor='forestgreen') #Campo de futbol
        circle = Circle((0,0),0.5,linewidth=1,edgecolor='black',facecolor='none')   #Circulo de medio
        line = Polygon(np.array([[0,-4.5],[0,4.5]]),closed=False,linewidth=1,edgecolor='black',facecolor='none')    #Linea del medio
        rectGoal1=Rectangle((-6.5,-0.6),0.5,0.6*2,linewidth=2,edgecolor='black',facecolor='forestgreen')   #Arco 1
        rectGoal2=Rectangle((6,-0.6),0.5,0.6*2,linewidth=2,edgecolor='black',facecolor='forestgreen')  #Arco 2
        rectPen1=Rectangle((-6,-1.25),1.25,1.25*2,linewidth=1,edgecolor='black',facecolor='none')   #Area de penal 1
        rectPen2=Rectangle((4.75,-1.25),1.25,1.25*2,linewidth=1,edgecolor='black',facecolor='none') #Area de penal 2
        ax=plt.gca()    #Se obtiene ele eje actual
        
        #Se ponen los elementos
        ax.add_patch(rect)
        ax.add_patch(circle)
        ax.add_patch(line)
        ax.add_patch(rectGoal1)
        ax.add_patch(rectGoal2)
        ax.add_patch(rectPen1)
        ax.add_patch(rectPen2)
        return ax
              
    def dist(self,p,q):
        return math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    def posCallBack(self,data):
        """Función callback para actualizar la posición del robot, la agrega al arreglo de posición
        Args:
            data (Twist): Posición del robot, la primera posición corresponde a X, la segunda a Y y la tercera la orientación
        """
        x,y,theta=data.linear.x,data.linear.y, data.angular.z
        self.robotPos.append([x,y,theta])
        if(len(self.robotPos)%5==0):
            self.ax.scatter(x,y,color="blue",zorder=10,marker=".") #Se guarda y se grafica la posicion del robot
        return
    
    def ballCallBack(self,data):
        """Función callback para tomar la posicion de la pelota
        Args:
            data (Float32MultiArray): Arreglo de dos posiciones con la ubicación de la pelota
        """
        if self.ballPos is None:    #Si es el primer dato que se recibe, se ejecuta
            #Se guarda la posicion de la pelota, que servira de posicion final
            self.ballPos=list(data.data)
            self.ax.scatter(self.ballPos[0],self.ballPos[1],marker=".",color="red",zorder=10)   #Se grafica para tener referencia de la pelota
            self.cancha = self.dist(self.ballPos,self.posGoal[0])>self.dist(self.ballPos,self.posGoal[1]) #Se determina en que cancha se tiene que hacer gol, 
                                                                                                          #dependiendo de a cual este más cerca
            if self.cancha: #Se borra la posicion de la cnacha con la cual no se va a hacer gol
                 self.posGoal.remove(self.posGoal[0])
            else:
                self.posGoal.remove(self.posGoal[1])
        return
    
    def control(self):
        
        #Variables para tener en cuenta en el control
        print('Arco donde anotar: ',self.posGoal)
        bdx,bdy = self.posGoal[0][0] - self.ballPos[0],self.posGoal[0][1] - self.ballPos[1] #Se calculan las componentes de un vector arco-pelota
        bangle = math.atan2(bdy,bdx)  #Dirección del vector, esta sera la orientación final del robot. Repsuesta en radianes desde -pi hasta pi
        deltaError=0.075
        msg = Twist()
        
        #Posición del robot y orientacion
        posBall = self.ballPos
        robotPos = self.robotPos[-1][0:2]
        robotOr = self.robotPos[-1][2]
        print('Posición balon: ',posBall)
        
        #Casos sencillos
        #Se va a determinar la posicion final del robot
        dr=0.25
        posF=[0,0]
        a = math.pi-abs(bangle)
        if posBall[0]>=0 and posBall[1]>=0:
            print('Caso 1')
            posF[0] = posBall[0]+dr*math.cos(a)
            posF[1] = posBall[1]+dr*math.sin(a)
        elif posBall[0]>=0 and posBall[1]<0:
            print('Caso 2')
            posF[0] = posBall[0]+dr*math.cos(a)
            posF[1] = posBall[1]-dr*math.sin(a)
        elif posBall[0]<0 and posBall[1]>=0:
            print('Caso 3')
            posF[0] = posBall[0]+dr*math.cos(a)
            posF[1] = posBall[1]+dr*math.sin(a)
        elif posBall[0]<0 and posBall[1]<0:
            print('Caso 4')
            posF[0] = posBall[0]+dr*math.cos(a)
            posF[1] = posBall[1]-dr*math.sin(a)

        print('Posición Destino: ',posF)
        
        
        dx = posF[0]-robotPos[0]
        dy = posF[1]-robotPos[1] #Componentes del vector del robot a la pelota
        
        #Se va hacer un control en 4 fases.
        #1-Se va a llevar al robot a orientacion 0°
        #2-Se va a ubicar el robot en el eje X
        #3-Se va a ubicar el robot en la posicion en Y
        #3-Se va a orientar el robot hacia la orientación deseada
        
        erS1= robotOr #Error etapa 1
        erS2 = dx       #Errores etapa 2 y 3
        erS3 = dy
        erS4=robotOr-bangle  #Error etapa 4
        step= -10
        
        #Se determina en que etapa de control esta
        if abs(erS1)>=deltaError:
            step=1
        elif abs(erS2)>=deltaError:
            step=2
        elif abs(erS3)>=deltaError:
            step=3
        if abs(erS4)>=deltaError and abs(erS2)<deltaError and abs(erS3)<deltaError:
            step=4
        if abs(erS2)<deltaError and abs(erS3)<deltaError and abs(erS4)<deltaError:
            self.end=True
            step=-1
        
        print('Error S1',erS1)
        print('Error S2',erS2)
        print('Error S3',erS3)
        print('Error S4',erS4)
        print('Paso',step)
        
        if step==1:
            msg.angular.z=-erS1*self.K[2]
        elif step==2:
            msg.linear.y = erS2*self.K[0]
        elif step==3:
            msg.linear.x = erS3*self.K[1]
        elif step==4:
            msg.angular.z=-erS4*self.K[2]
        
        
        self.pub[1].publish(msg)    #Se publica el comando
        
        
        
            
        

        
    
if __name__=="__main__":
    x = soccerRobot([0.25,0.25,0.1])
    x()
    