#!/usr/bin/env python
# coding: latin-1
import sys,rospy,os,tf,math
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class controlNode():
    
    def __init__(self,K,posF, escala):
        """Metodo Creacion del Nodo
        Args:
            K ([int]): Arreglo con las constantes de control
            posF([int]): Arreglo con la pose final del robot
        """

        #Nombre del Nodo
        self.nombre = 'Senecabot_drawer'

        #Escala de la imagen
        self.scale = escala;

        #TPublisher
        self.pub = rospy.Publisher('cmd_vel',Twist,queue_size=70)
        rospy.Subscriber('odom',Odometry,self.odomCallBack)

        #Posicion del robot. X y Y son lineares. Z es angular
        self.x = [0]
        self.y = [0]
        self.z = [0]
        self.c = 1;

        #Constantes para control del robot
        assert  len(K)==2,"El arreglo de constantes de control no posee exactamente 2 valores" 
        self.K = K

        #Variable de control para saber sia acabo el recorrido
        self.end = False


        #assert len(posF)==3,"La posición final no tiene 3 entradas"
        #assert all(isinstance(x,(float,int)) for x in posF),"Los datos ingresados no son numericos"
        
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
        self.posFS = posF;
        self.posF = [];
        self.estadoDir = 1;
        self.antDist = 100;
        self.antAng = 100;
        self.antTime = 0;
        self.antVel = 0;
        self.controlState = 1;
        return

        
    def __call__(self):
        """Metodo Call para cuando se llame una variable de controlNode
        """
        rospy.loginfo("Se iniciara el Nodo")
        rospy.init_node(self.nombre,anonymous=True)       #Inicializacion del Nodo
        self.rate = rospy.Rate(8)

        for p in self.posFS:
            self.posF = [float(i)/self.scale for i in p.replace('[','').replace(']','').split(',')];      
            for idx,val in enumerate(self.posF):
                if idx%2==0 and idx>1:
                    self.posF[idx]=np.pi/2
            print(self.posF);
            
            #En este loop se ejecuta el algoritmo de control
            while not (rospy.is_shutdown() and not self.end):
                self.control()
                self.rate.sleep()
            self.end = False;

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
        dist = math.sqrt(dx**2 + dy**2);
        #dist = abs(dx) + abs(dy);
        beta = Z - math.atan2(pos[1], pos[0]);   #Diferenia angulo cerrado

        #print('Pose actual')
        #print(X,Y,Z)

        if(abs(beta)>=0.08 and self.controlState == 1):
            if(beta == self.antAng):
                msg.angular.z=0;
                self.controlState = 2;
            else:    
                print("Estado W", beta, self.antAng, -Kb*(beta));
                msg.angular.z=-Kb*(beta);
                self.antAng = beta;

        elif(abs(beta)<=0.08 and self.controlState == 1):
            self.controlState = 2;
        
        elif(abs(dist) >= deltaError and self.controlState == 2):
            print("Estado X", dist, self.antDist, Kp*dist*self.estadoDir);

            msg.linear.x=Kp*dist*self.estadoDir;

            if(dist > self.antDist and self.estadoDir == 1):
                self.estadoDir = self.estadoDir * -1;
            elif(dist > self.antDist and self.estadoDir == -1):
                self.controlState = 3;
            elif(dist == self.antDist):
                self.controlState = 3;

            self.antDist = dist;

        elif(abs(dist) <= deltaError or self.controlState == 3):
            self.end = True;
        
        #rospy.loginfo(msg)  
        self.pub.publish(msg);

if __name__=='__main__':
    try:
        posFS = [];
        K = [2.5,1.5];
        escala = 0.5;

        if len(sys.argv) > 1:
            posFS = sys.argv[1].split(";");
        else:
            print("Qué figura quiere dibujar? \n Pez \n Toro \n");
            file = raw_input("Ingrese la figura: ").lower() + ".txt";
            name = 'senecabot_drawer.py';
            path = os.path.abspath(__file__).replace("scripts"+os.path.sep+name, "docs"+os.path.sep+file);
            f = open(path, "r");
            posFS = f.read().split(";");

        nodo = controlNode(K, posFS, escala);
        nodo();

    except ValueError:
        print('No se ingreso coordenadas Finales');
    except AssertionError:
        print('Error de Precondiciones');
        raise
    except:
        print("No ingrsó una figura correcta");
        raise