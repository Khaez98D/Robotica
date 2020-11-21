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
        self.pub = rospy.Publisher('cmd_vel',Twist,queue_size=70)
        rospy.Subscriber('odom',Odometry,self.odomCallBack)

        #Posicion del robot. X y Y son lineares. Z es angular
        self.x = []
        self.y = []
        self.z = []
        self.c = 1;

        #Constantes para control del robot
        assert  len(K)==2,"El arreglo de constantes de control no posee exactamente 2 valores" 
        self.K = K

        #Variable de control para saber sia acabo el recorrido
        self.end = False


        assert len(posF)==3,"La posición final no tiene 3 entradas"
        assert all(isinstance(x,(float,int)) for x in posF),"Los datos ingresados no son numericos"
        
        '''
        Z=0
        if round(posF[1])>0:
            Z=np.pi/2
        elif round(posF[1])<0:
            Z=-np.pi/2
        elif round(posF[0])<0:
            Z=-np.pi


        posF.append(Z)
        '''
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

        print("Termino la ejecucion");   #Notificación a consola


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
        deltaError=0.05    #Se define las constantes de control
        pos = self.posF    #Se obtiene la posición Final
        X,Y,Z=self.x[-1],self.y[-1],self.z[-1]   #Se obtiene las posiciones actuales del robot
        dx = pos[0]-X    #Diferencia en X
        dy = pos[1]-Y     #Diferencia en Y
        beta = -Z-posF[2]   #Diferenia angulo cerrado
        controlState=-1     #Estado de control

        #print('Pose actual')
        #print(X,Y,Z)

        
        if(abs(dy)>=deltaError) and self.c%2 == 0:
            print("Estado Y")
            #msg.linear.x=Kp*dx
            msg.linear.y=Kp*dy
            #msg.angular.z=-Kb*beta
            self.c += 1;
        elif(abs(dx)>=deltaError):
            print("Estado X")
            msg.linear.x=Kp*dx
            #msg.linear.y=Kp*dy
            #msg.angular.z=-Kb*beta
            self.c += 1;
        elif(abs(dx)<=deltaError) and (abs(dy)<=deltaError):
            if(abs(beta)>=deltaError+0.1):
                print("Estado W")
                msg.angular.z=-Kb*abs(beta)
                self.c += 1;
            else:
                self.end=True;
        
        rospy.loginfo(msg)  
        self.pub.publish(msg)

if __name__=='__main__':
    try:
        if len(sys.argv)==2:
            posF = [float(i) for i in sys.argv[1].replace('[','').replace(']','').split(',')]
            K = [3,2.5]
            nodo = controlNode(K,posF)
            nodo()
        else:
            raise ValueError()
    except ValueError:
        print('No se ingreso coordenadas Finales');
    except AssertionError:
        print('Error de Precondiciones');