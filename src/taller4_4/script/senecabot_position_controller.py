#!/usr/bin/env python
import sys,rospy,os,tf
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class controlNode():
    
    def __init__(self,K):
        """Metodo Creacion del Nodo
        Args:
            K ([int]): Arreglo con las constantes de control
        """

        #Nombre del Nodo
        self.nombre = 'Senecabot_Position_Controller'

        #TPublisher
        self.pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
        rospy.Subscriber('odom',Odometry,odomCallBack)

        #Posicion del robot. X y Y son lineares. Z es angular
        self.x = []
        self.y = []
        self.z = []

        #Constantes para control del robot
        assert (len(K)==3),"El arreglo de constantes de control no posee exactamente 3 valores"
        self.K = K


        #Variable de control para saber sia acabo el recorrido
        self.end = False


        return

        
    def __call__(self):
        """Metodo Call para cuando se llame una variable de controlNode
        """
        rospy.loginfo("Se iniciara el Nodo")
        rospy.init_node(self.name,anonymous=True)       #Inicializacion del Nodo
        self.rate= rospy.Rate(10)

        #En este loop se ejecuta el algoritmo de control
        while not (rospy.is_shutdown() or self.end):
            self.control()
            self.rate.sleep()

        print("Termino la ejecución")   #Notificación a consola


    def odomCallBack(self,data):
        """Función CallBack para el topico de odometria. Transforma de Cuaterniones a angulos de Euler.
        Guarda la orientación del robot en el arreglo de Z.
        Args:
            data (Quaternion): Orientación del robot en cuaterniones
        """
        euler = euler_from_quaternion([pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w])
        self.z.append(euler[2])

    def control(self):
        """Metodo para generar el control del robot
        """
        pass

if __name__=='__main__':
    pass