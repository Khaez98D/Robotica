#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import Twist,Vector3
from std_msgs.msg import Float32
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
      
class listenerNode():

    def __init__(self):
        #Se crean arreglos para almacenar las coordenadas XYZ y la orientación
        self.x,self.y,self.z,=[],[],[]
        self.theta=0
        
        #Contador de longuitud de arreglo
        self.length = 0
        self.fig,self.ax = plt.subplots()
        self.ax.set_title("Ubicacción del TurtleBot")
        self.ax.set_xlabel("X(m)")
        self.ax.set_ylabel("Y(m)")
        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.grid(True)
        
        #Se inicia el nodo para que tome los datos de posicion y orientación
        rospy.init_node('listener',anonymous=True)
        rospy.Subscriber('turtlebot_position',Twist,self.updatePos)
        
        plt.show()
        rospy.spin()
        return       
        

    #Funcion Callback para agregar datos al arrelgo de posición
    def updatePos(self,data):
        self.length+=1
        self.x.append(data.linear.x)
        self.y.append(data.linear.y)
        self.z.append(data.linear.z)
        
        #Inicializar grafica
        if(len(self.x)%10==0):
            self.ax.plot(self.x[:-1],self.y[:-1],color="red",alpha=1,linewidth=2)
            plt.draw()
        return
    
    
if __name__ == "__main__":
    listenerNode()
    plt.savefig('/home/robotica/catkin_ws/src/turtle_bot_4/results/trayectoria_punto2.png')