#!/usr/bin/env python3
import sys,rospy,os
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray


#Clase Listener para escuchar la posición del robot
class Position():

    #Función que construye el nodo PositionListener
    def __call__(self):
        #Se inicializa el nodo
        rospy.Subscriber('turtlebot_position',Twist,self.updatePos)
        self.OdometryPipe =[]
        self.Topic=[]  
        self.updateGraph()
        rospy.spin()
        return
    
    
    def updatePos(self,data):
        self.Topic.append([data.linear.x,data.linear.y])
        pass

    #Función para actualizar la grafica sacando los datos del pipe
    def updateGraph(self):
        x=None
        plt.grid(True) #Inicializacion de la grafica
        plt.xlabel("Posición en X (m)")
        plt.xlabel("Posición en Y (m)")
        x=self.OdometryPipe
        if(len(x)%5==0):
            pass
        x=self.Topic
        if(len(x)%5==0):
            plt.plot(x[:,0],x[:,1],label='Topico',marker="-o-") #Se grafica
        
    #Se muestra la grafica y se guarda
    plt.draw()
    plt.pause(0.01)
    plt.legend()
    plt.savefig('prueba.jpg')
    plt.clf()