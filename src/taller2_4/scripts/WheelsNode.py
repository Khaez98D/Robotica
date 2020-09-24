#!/usr/bin/env python3
import sys,rospy,os
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray


#Clase para el Talker de las velocidades lineales de las ruedas
class wheelsVel():    
    
    
    def __init__(self,rutaArchivo):
        self.rutaArchivo=rutaArchivo
    
    #Función de inicialización
    #Param: rutaArchivo, la ruta del archivo de texto
    def __call__(self):       
        #Se crea e inicializa el nodo
        self.pub = rospy.Publisher('/turtlebot_wheelsVel',Float32MultiArray,queue_size=10)          
        #Se obitienen los datos del archivo de texto
        self.data=self.getData(self.rutaArchivo)
        self.rates=rospy.Rate(10)
        i=0 #Contador de cuantas lineas hay que leer
        while (not rospy.is_shutdown()) and i<len(self.data): #Ciclo, si i>len(data), significa que ya termino de leer el archivo
            t,tv = 0,self.data[i][2]    #Contador de tiempo y tiempo durante el cual se aplica el perfil de velocidad
            print("Se va a mandar el mensaje: ",self.data[i][0:2]) #Se notifica por consola
            while t<tv:
                self.pub.publish(Float32MultiArray(data=self.data[i][0:2])) #Se publica el mensaje
                t+=1 #Sube uno el contador de tiempo
                rospy.sleep(1)  #Se duerme durante un segundo
                self.rates.sleep()  #Se duerme el rate al que se mandan los mensajes
            i+=1 #Se suma 1 a la linea que se leyo
        self.pub.publish(Float32MultiArray(data=[0,0])) # Al acabar se manda este mensaje para parar el robot
    
    
    #Función que extrae los datos del archivo
    #Param: rutaArchivo, la ruta al archivo
    #Return: data, matriz de n filas y 3 columnas, contiene los perfiles de velocidad y el tieempo de aplicacion de las n lineas
    def getData(self,rutaArchivo):
        with open(rutaArchivo,mode='r') as reader: #Se lee el archivo
            lines = reader.readlines()             #Se obtienen todas las lineas
            data=[0 for i in range(int(lines[0]))]  #Se inicializa el arreglo para N lineas
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
    rospy.init_node('MovementNode',anonymous=True)
    try:
        if len(sys.argv)==2:   #La segunda posicion del arreglo es el nombre del archivo
            ruta=verificarRutaArchivo(sys.argv[1])  #Se encuentra la ruta al archivo
            x=wheelsVel(ruta)
            x()     
            
        else: 
            raise FileExistsError #Se genera error si el archivo no existe
    #Excepts para manejo de los errores
    except FileExistsError:
        print("El nombre del archivo no es valido")
    except rospy.ROSInterruptException:
        print("Se interrumpio ROS")


