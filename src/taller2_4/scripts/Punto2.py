#!/usr/bin/env python3
import sys,rospy,os
import numpy as np
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray,Float32

#Clase para el nodo
class PublisherListenerNode():
    
    #Función de creacion del nodo. Se inicializan las variables a usar
    def __init__(self,rutaArchivo):
        self.n = 0                                  #Numero de lineas que se deben leer del archivo
        self.data=self.getData(rutaArchivo)         #Se carga el arhivo en una estructura de datos para que despues sea leido
        self.xT,self.yT=[],[]                       #Se crean los arreglos que van a guardar la información de la posición obtenida por el Topico
        self.xO,self.yO=[],[]                       #Se crean los arreglos que van a guardar la información de la posición obtenida por Odometria
        self.errX,self.errY=[],[]                   #Se crean arreglos para guardar los errores
        self.time,self.time0=[],0                   #Arreglo para almacenar el tiempo
        self.fig,self.ax = plt.subplots()           #Figura para graficar la posición
        self.fig2,self.ax2 = plt.subplots()         #Figura para graficar el error
        
        self.pub = rospy.Publisher('/turtlebot_wheelsVel',Float32MultiArray,queue_size=10)     #Publisher del nodo
        rospy.Subscriber('turtlebot_position',Twist,self.callbackPosition)                           #Listener del nodo
        rospy.Subscriber('/simulationTime',Float32,self.callbackTime)
        self.end=False                              #Variable que indica si el sistema acabo
        self.G1Path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'results/trayectoria_punto3.png')
        self.G2Path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'results/error_punto3.png')
        return
     
     
    #Función para cuando se llama el objeto. Con esta funcion se inizaliza el nodo y sus funciones
    def __call__(self):
        rospy.init_node('MovementNode',anonymous=True)
        self.rate = rospy.Rate(10)                  #Rate de actualización de 10Hz
        #Crear grafica, con su titulo, ejes y limites
        self.ax.set_title("Ubicacción del TurtleBot")
        self.ax.set_xlabel("X(m)")
        self.ax.set_ylabel("Y(m)")
        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.grid(True)
        plt.ion()
        plt.show()
        #Se duerme un segundo la grafica y rospy para poder que se inicalice corretamente
        plt.pause(1)
        rospy.sleep(1)
        
        aux=0   #Variable auxilar para poner los legends
        print("Va a comenzar el movimiento del robot")  #Notificación a consola
        while (not rospy.is_shutdown()) and (not self.end):
            if(aux==0): #Si es la primera entrada, se ponen los ejes
                self.actualizar()
                plt.legend()
                aux+=1
                plt.pause(1/100)    #FrameRate para actualizar la graficac
            self.publicar()         #Se publica el mensaje
        plt.savefig(self.G1Path)
    
    
    #Metodo para publicar el mensaje
    def publicar(self):
        #Se coloca en un try, para aprovechar el uso de Finally:
        try:
            i=len(self.data)-self.n     #Indice de la linea a obtener
            if i<len(self.data):            #Si no se han leido todas las lineas
                x=np.array(self.data[i])    #Datps de la linea
                t,tv = 0,self.data[i][2]    #Contador de tiempo y tiempo durante el cual se aplica el perfil de velocidad
                print("Se va a mandar el mensaje:", x[0:2]) #Notificación del mensaje a enviar
                while t<tv:
                    self.actualizar()      #Se actualiza la grafica
                    plt.pause(1/100)       #FrameRate
                    self.pub.publish(Float32MultiArray(data=x[0:2])) #Se publica el mensaje
                    t+=1 #Sube uno el contador de tiempo
                    rospy.sleep(1)  #Se duerme durante un segundo
                    self.rate.sleep()  #Se duerme el rate al que se mandan los mensajes
                    self.actualizar()   #Se actualiza la grafica
                    plt.pause(1/100)    #FrameRate
                self.n-=1   #Se resta 1 a las lineas totales
            else:
                self.end=True   #Si se acabaron las iteraciones, se rompe el ciclo de call
            return
        finally:
            self.actualizar()   #Se actualiza la grafica al final de todos los trayectos
            plt.pause(1/100)    #FrameRatte
            self.pub.publish(Float32MultiArray(data=np.array([0,0])))   #Se frena el robot un momento, para asegurar el correcto funcionamiento
    
    #Función que obtiene el tiempo de simulación normalizado, el T0 se toma con respecto a la primera medición de tiempo que se tuvo
    def callbackTime(self,data):
        if(len(self.time)==0):  #Si es el primer item
            self.time.append(data.data-data.data) #Se agrega como 0, por que es el primer instante
            self.time0=data.data                  #Se guarda su referencia para normalizar
        else:
            self.time.append(data.data-self.time0)  #Se guarda el tiempo normalizado
    
    #Funcion que almacena la posición en los arreglos, y calcula el error
    def callbackPosition(self,data):
        self.xT.append(data.linear.x)   #Se agregan el dato leido por el topico
        self.yT.append(data.linear.y)
        #odometria()                    #Se hace el calculo por odometria
        #self.errX.append(abs(self.xT[-1]-self.xO[-1]))      #Se agregan los errores
        #self.errY.append(abs(self.yT[-1]-self.yO[-1]))
        
    
    #Metodo para actualziar la grafica
    def actualizar(self):  
        if(len(self.xT)>0): #Se grafica si se tiene mas de un item
            self.ax.scatter(self.xT,self.yT,label="Posición obtenida del topico",marker=".",color="blue")
            plt.draw()
        if(len(self.xO)>0):
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
    
    
    #Función que calcula la matriz de rotación respeccto a un angulo O
    def R(self,o):
        return np.array([
            [np.cos(o),np.sin(o),0],
            [-np.sin(o),np.cos(o),0],
            [0,0,1]
        ])
        
    #Función que calcula la matriz de rotación inversa respeccto a un angulo O
    def Rinv(self,o):
        return np.array([
            [np.cos(o),-np.sin(o),0],
            [np.sin(o),np.cos(o),0],
            [0,0,1]
        ])
    
    
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