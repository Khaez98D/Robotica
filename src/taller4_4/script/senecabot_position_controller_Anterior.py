#!/usr/bin/env python
# coding: latin-1
import sys,rospy,os,tf,math
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class controlNode():
    
    def __init__(self,K,posF):
        """Metodo Creacion del Nodo
        Args:
            K ([int]): Arreglo con las constantes de control
            posF([int]): Arreglo con la pose final del robot
        """

        #Nombre del Nodo
        self.nombre = 'Senecabot_Position_Controller'

        #TPublisher
        self.pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
        rospy.Subscriber('odom',Odometry,self.odomCallBack)

        #Posicion del robot. X y Y son lineares. Z es angular
        self.x = []
        self.y = []
        self.z = []

        #Constantes para control del robot
        assert  len(K)==2,"El arreglo de constantes de control no posee exactamente 2 valores" 
        self.K = K

        #Variable de control para saber sia acabo el recorrido
        self.end = False


        assert len(posF)==2,"La posición final no tiene dos entradas"
        assert all(isinstance(x,(float,int)) for x in posF),"Los datos ingresados no son numericos"
        
        Z=0
        if round(posF[1])>0:
            Z=np.pi/2
        elif round(posF[1])<0:
            Z=-np.pi/2
        elif round(posF[0])<0:
            Z=-np.pi


        posF.append(Z)
        self.posF=posF
        return

        
    def __call__(self):
        """Metodo Call para cuando se llame una variable de controlNode
        """
        rospy.loginfo("Se iniciara el Nodo")
        rospy.init_node(self.nombre,anonymous=True)       #Inicializacion del Nodo
        self.rate= rospy.Rate(10)

        #En este loop se ejecuta el algoritmo de control
        while not (rospy.is_shutdown() or self.end):
            self.control()
            self.rate.sleep()

        print "Termino la ejecucion"   #Notificación a consola


    def odomCallBack(self,data):
        """Función CallBack para el topico de odometria. Transforma de Cuaterniones a angulos de Euler.
        Guarda la orientación del robot en el arreglo de Z.
        Args:
            data (Quaternion): Orientación del robot en cuaterniones
        """
        pose = data.pose.pose
        self.x.append(pose.position.x)
        self.y.append(pose.position.y)
        euler = euler_from_quaternion([pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w])
        self.z.append(euler[2])

    def control(self):
        """Metodo para generar el control del robot
        """
        msg = Twist()    #Se ccrea el mensaje de odometria
        Kp,Kb = self.K      #Se obtienen las constantes
        deltaError=0.075    #Se define las constantes de control
        pos = self.posF    #Se obtiene la posición Final
        X,Y=self.x[-1],self.y[-1]   #Se obtiene las posiciones actuales del robot
        dx = pos[0]-X     #Diferencia en X
        dy = pos[1]-Y     #Diferencia en Y
        rho = math.sqrt((dx**2)+(dy**2))  #Distancia a recorrer
        alfa = -self.z[-1]+np.arctan2(dy,dx)    #Angulo entre la pose actual del robot y el punto al cual llegar
        beta = -self.z[-1]-posF[2]   #Diferenia angulo cerrado
        controlState=-1     #Estado de control

        
        #Se determina cual es el estado de control
        if abs(beta)>=deltaError:
            controlState=1
        elif abs(rho)>=deltaError:
            controlState=2
        else:
            self.end=True
        

        posActual = "\n Posición Actual : ["+str(X)+","+str(Y)+","+str(self.z[-1])+"]"
        log = "\n Estado de control: " + str(controlState) + "\n Beta = " + str(beta) + "\n Rho = " +str(rho)
        d = "\n dx = " + str(dx) + "\n dy = " +str(dy) + "\n alfa = " +str(alfa)
        rospy.loginfo(posActual)
        rospy.loginfo(log)
        rospy.loginfo(d)


        
        #Se hace el control
        if controlState==1:
            msg.angular.z = -Kb*beta #Se ubica la orientación del robot a la orientacion final
        elif controlState==2:
            V = rho* Kp  #Se determina la velocidad
            #msg.linear.x = V*np.cos(alfa)   #Se descompone el vector en X y Y segun el angulo entre la pose actual y la distancia al objetivo
            #msg.linear.y = V*np.sin(alfa)
            msg.linear.y = -V*np.cos(alfa)   #Se descompone el vector en X y Y segun el angulo entre la pose actual y la distancia al objetivo
            msg.linear.x = V*np.sin(alfa)
        
        rospy.loginfo(msg)  
        self.pub.publish(msg)

if __name__=='__main__':
    try:
        if len(sys.argv)==2:
            posF = [float(i) for i in sys.argv[1].replace('[','').replace(']','').split(',')]
            K= [0.75,0.5]
            nodo = controlNode(K,posF)
            nodo()
        else:
            raise ValueError()
    except ValueError:
        print 'No se ingreso coordenadas Finales'
    except AssertionError:
        print 'Error de Precondiciones'