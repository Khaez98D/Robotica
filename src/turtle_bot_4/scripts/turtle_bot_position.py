#!/usr/bin/env python3
import rospy,atexit,os
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
        self.topicName='/turtlebot_position'
        self.FolderPath=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'results/trayectoria_punto2.png')
       
        
        #Se inicia el nodo para que tome los datos de posicion y orientación
        if(self.checkTopic()):
            rospy.init_node('listener',anonymous=True)
            rospy.Subscriber('turtlebot_position',Twist,self.updatePos)
            plt.show()
            rospy.spin()
        else: return       
        

    #Funcion Callback para agregar datos al arrelgo de posición
    def updatePos(self,data):
        if(self.checkTopic()):
            self.length+=1
            self.x.append(data.linear.x)
            self.y.append(data.linear.y)
            self.z.append(data.linear.z)
        
            #Inicializar grafica
            if(len(self.x)%10==0):
                self.ax.plot(self.x[:-1],self.y[:-1],color="red",alpha=1,linewidth=2)
                plt.savefig(self.FolderPath,transparent=False)
                plt.draw()
            return
        else:
            raise Exception
            
    
    def checkTopic(self):
        topics=rospy.get_published_topics()
        for topic in topics:
            if(topic[0]==self.topicName):
                return True      
        return False


        
if __name__ == "__main__":
    try:
        listenerNode()
    except Exception as err:
        pass
    finally:
        pass