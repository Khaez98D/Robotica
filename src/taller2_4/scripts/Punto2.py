#!/usr/bin/env python3
import sys,rospy,os
import numpy as np
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray


class PublisherListenerNode():
    
    #Función de creacion del nodo. Se inicializan las variables a usar
    def __init__(self,rutaArchivo):
        self.n = 0                                  #Numero de lineas que se deben leer del archivo
        self.data=self.getData(rutaArchivo)         #Se carga el arhivo en una estructura de datos para que despues sea leido
        self.xT,self.yT=[],[]                       #Se crean los arreglos que van a guardar la información de la posición obtenida por el Topico
        self.xO,self.yO=[],[]                       #Se crean los arreglos que van a guardar la información de la posición obtenida por Odometria
        self.errX,self.errY=[],[]                   #Se crean arreglos para guardar los errores
        self.fig,self.ax = plt.subplots()           #Figura para graficar la posición
        self.pub = rospy.Publisher('/turtlebot_wheelsVel',Float32MultiArray,queue_size=10)     #Publisher del nodo
        rospy.Subscriber('turtlebot_position',Twist,self.actualizar)                           #Listener del nodo
        self.end=False                              #Variable que indica si el sistema acabo
        return
     
     
    #Función para cuando se llama el objeto. Con esta funcion se inizaliza el nodo
    def __call__(self):
        rospy.init_node('MovementNode',anonymous=True)
        self.rate = rospy.Rate(10)                  #Rate de actualización de 10Hz
        #Crear grafica
        self.ax.set_title("Ubicacción del TurtleBot")
        self.ax.set_xlabel("X(m)")
        self.ax.set_ylabel("Y(m)")
        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.grid(True)
        plt.ion()
        plt.show()
        while (not rospy.is_shutdown()) and (not self.end):
            self.publicar()
            rospy.sleep(0.1)
        print("Salio")
        
    def publicar(self):
        try:
            i=len(self.data)-self.n     #Indice de la linea a obtener
            if i<len(self.data):
                x=np.array(self.data[i])    #Datps de la linea
                t,tv = 0,self.data[i][2]    #Contador de tiempo y tiempo durante el cual se aplica el perfil de velocidad
                print("Se va a mandar el mensaje:", x[0:2])
                while t<tv:
                    self.pub.publish(Float32MultiArray(data=x[0:2])) #Se publica el mensaje
                    t+=1 #Sube uno el contador de tiempo
                    rospy.sleep(1)  #Se duerme durante un segundo
                    self.rate.sleep()  #Se duerme el rate al que se mandan los mensajes
                self.n-=1   #Se resta 1 a las lineas totales
            else:
                self.end=True
            return
        finally:
            self.pub.publish(Float32MultiArray(data=np.array([0,0])))
    
    def actualizar(self,data):
        plt.pause(1)
        self.xT.append(data.linear.x)   #Se agregan el dato leido por el topico
        self.yT.append(data.linear.y)
        #odometria()                    #Se hace el calculo por odometria
        #self.errX.append(abs(self.xT[-1]-self.xO[-1]))      #Se agregan los errores
        #self.errY.append(abs(self.yT[-1]-self.yO[-1]))
        if(len(self.xT)%5==0 and len(self.xT)>0):
            self.ax.scatter(self.xT[:-1],self.yT[:-1],label="Posición obtenida del topico",marker=".",color="blue")
            plt.draw()
        if(len(self.xO)%5==0 and len(self.xO)>0):
            self.ax.scatter(self.xO,self.yO,label="Posición obtenida por Odometria",marker=".",color="red")
            plt.draw()
        return
    
    #Función que calcula la posición por odometria
    def odometria(self):
        pass
    
    #Función que extrae los datos del archivo
    #Param: rutaArchivo, la ruta al archivo
    #Return: data, matriz de n filas y 3 columnas, contiene los perfiles de velocidad y el tieempo de aplicacion de las n lineas
    def getData(self,rutaArchivo):
        with open(rutaArchivo,mode='r') as reader: #Se lee el archivo
            lines = reader.readlines()             #Se obtienen todas las lineas
            self.n=int(lines[0])                   #Se le asigna un valor
            data=[0 for i in range(self.n)]  #Se inicializa el arreglo para N lineas
            for i in range(1,len(lines)):
                data[i-1] = [int(j) for j in lines[i].split()]  #Se sacan y organizan los datos
        return data     #Retorna la estructura de datos final
    
    
    
#Función para verificar la ruta de archivo, si no existe enviara exepcion
#Param: nombreArchivo, el nombre del archivo
#return: Ruta absoluta del archivo
#Throws: FileExistError si el archivo no existe
def verificarRutaArchivo(nombreArchivo):
    directorioPadre=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(directorioPadre,'resources/'+nombreArchivo)
    if(os.path.isfile(ruta)):
        return ruta
    else:
        raise FileExistsError
    
#Metodo Main           
if __name__ == "__main__":
    ruta=''
    try:
        if len(sys.argv)==2:   #La segunda posicion del arreglo es el nombre del archivo
            ruta=verificarRutaArchivo(sys.argv[1])  #Se encuentra la ruta al archivo
            print("El nombre del archivo es:", ruta)
            x=PublisherListenerNode(ruta)
            x()   
        else: 
            raise FileExistsError #Se genera error si el archivo no existe
    #Excepts para manejo de los errores
    except FileExistsError:
        print("El nombre del archivo no es valido")
    except rospy.ROSInterruptException:
        print("Se interrumpio ROS")