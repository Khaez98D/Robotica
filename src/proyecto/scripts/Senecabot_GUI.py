#!/usr/bin/python
# coding: latin-1

import cv2
import rospy
import pygame
import os
import pygame
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from proyecto.srv import *
from tools import Tools
from std_msgs.msg import Float32MultiArray, Float32,String

os.environ['SDL_AUDIODRIVER'] = 'dsp'
PATHPLANO = r'/home/robotica/catkin_ws/src/proyecto/docs/Gridmap.png'  # Path a la imagen del plano
puntoInicial = []  # Coordenadas punto inicial
puntoFinal = []  # Coordenadas punto final



class servicioPuntos:

    '''
    Clase que provee el servicio de informar los puntos iniciales y finales
    '''

    def handleResponse(self, req):
        '''
        Metodo que informa las coordeanadas
        '''

        resp = str(self.puntos[0])+','+str(self.puntos[1])
        return pointsResponse(resp)

    def __init__(self, puntos):
        '''
        Metodo que inicializa el servidor
        '''

        self.puntos = puntos
        s = rospy.Service('Coordenadas', points, self.handleResponse)
        print 'Listo para informar coordenadas inicial y final'

class nodosVisitado:

    '''
    Clase que recibe las celdas de la planeacion de ruta
    '''

    def __init__(self, GUI):
        '''
        Se inicializan dos subscriptores, uno para obtener la ruta y el otro para dibujar los nodos visitados
        '''
        rospy.Subscriber('/senecabot_visited', Float32MultiArray,
                         self.callbackVisited)
        self.GUI = GUI

    def callbackVisited(self, data):
        '''
        Funcion callback para los nodos seleccionados
        '''
        dataCoord = data.data
        coord = (dataCoord[1], dataCoord[0])
        self.GUI.nodosVisitados(coord)

class nodosRuta:

    '''
    Clase que recibe las celdas de la planeacion de ruta
    '''

    def __init__(self, GUI):
        '''
        Se inicializan dos subscriptores, uno para obtener la ruta y el otro para dibujar los nodos visitados
        '''
        rospy.Subscriber('/senecabot_route', Float32MultiArray,
                         self.callbackRoute)
        self.GUI = GUI

    def callbackRoute(self, data):
        '''
        Funcion callback para la ruta seleccionada
        '''
        dataCoord = data.data
        coord = (dataCoord[1], dataCoord[0])
        self.GUI.nodosRuta(coord)

class ubicaion:

    '''
    Clase que grafica sobre el mapa la posicion actual del robot
    '''

    def __init__(self,GUI,start):
        '''
        Funcion que inicializa el subscriptor a odom
        '''
        rospy.Subscriber('/odom',Odometry,self.odomCallBack)
        self.start = tuple(start)[::-1]
        self.GUI = GUI
        self.x,self.y=self.start

    def odomCallBack(self,data):
        """Función CallBack para el topico de odometria. Transforma de Cuaterniones a angulos de Euler.
        Guarda la orientación del robot en el arreglo de Z.
        Args:
            data (Quaternion): Orientación del robot en cuaterniones
        """
        pose = data.pose.pose
        tolX = (3.5/700)*5 #Medida en metros, si se mueve más de tolX, se actualiza la interfaz con un corrimiento de 5 pixeles
                            #Valor calculado como: (LonguitudXReal/WithImagen) * numPixelesCorrimiento
        tolY = (3/600)*5 #Medida en metros, si se mueve más de tolY, se actualiza la interfaz con un corrimiento de 5 pixeles
                            #Valor calculado como: (LonguitudYReal/HeightImagen) * numPixelesCorrimiento
        (X,Y) = pose.position.x+self.start[0],pose.position.y+self.start[1] #Se suma las coordenadas del comienzo a la distancia recorrida
        
        """
        if abs(X-self.x)>=tolX or abs(Y-self.y)>=tolY:
            (self.x,self.y)=(X,Y)
            self.GUI.updatePos((int(Y),int(X)))     #Se aproxima al entero más cerano
        """
        self.GUI.updatePos((int(Y),int(X)))     #Se aproxima al entero más cerano

class aprilTag:

    '''
    Clase para determinar el april tag
    '''

    def __init__(self, GUI):
        rospy.Subscriber('/senecabot_tag', String)
        self.GUI = GUI
        self.tag = ''

    def callbackTag(self, data):
        tag = data.data
        if tag != self.tag:
            self.tag = tag
            self.GUI.updateAprilTag(tag)

class contador_monedas:

    '''
    Clase para determinar la cuenta de monedas
    '''

    def __init__(self, GUI):
        rospy.Subscriber('/senecabot_coins', String)
        self.GUI = GUI
        self.coin = ''

    def callbackTag(self, data):
        coin = data.data
        if coin != self.coin:
            self.coin=coin
            self.GUI.updateCoinCount(coin)

class cv2manager:

    '''
    Clase para manejar todo lo relacionado con cv2
    '''

    def __init__(self, path):
        self.img = cv2.imread(PATHPLANO, 0)
        self.img = cv2.blur(self.img,(5,5));
        self.shape = self.img.shape
        self.puntos = []
        self.imgWinName = 'Seleccion Puntos'

    def seleccionarPuntos(self):
        '''
        Metodo que retorna los puntos iniciales y finales
        '''

        cv2.namedWindow(self.imgWinName)  # Se asigna el nombre a la ventana
        cv2.imshow(self.imgWinName, self.img)  # Se muestra la imagen

        def mouseHandler(event,x,y,flags,params):
            '''
            Funcion callback para eventos de del mouse
            '''

            if event == cv2.EVENT_LBUTTONUP:
                if len(self.puntos) == 0:
                    self.puntos.append([x, y])
                elif len(self.puntos) == 1:
                    self.puntos.append([x, y])
                    cv2.destroyAllWindows()

        cv2.setMouseCallback(self.imgWinName, mouseHandler)  # Se le asigna la funcion callback a la ventana
        print 'Selecccione el punto inicial y el punto final'
        cv2.waitKey()
        return self.puntos

class GUI_manager:

    '''
    Clase que maneja la interfaz de PyGame
    '''

    def __init__(self, shape, coords):
        '''
        Metodo que inicializa el canvasde PyGame
        '''
        image = pygame.image.load(PATHPLANO)    #Se carga el plano como imagen
        
        self.tag = '0'  #Valor inicial del tag
        self.coin = '0'
        (self.h, self.w) = shape    #Se obtiene el tamaño del plano
        self.isPainted = [[False for j in range(self.w)] for i in range(self.h)]   #Matriz para no sobreponer pintura de visitados y ruta
        
        (self.start, self.goal) = coords    #Coordenadas de inicio y final, se transorman en tuplas y se invierten para que quede (Y,X)
        self.start = tuple(self.start)[::-1]
        self.goal = tuple(self.goal)[::-1]

        self.prob_free = 0.3
        self.prob_occ = 0.6

        self.size_win_x = int(self.w * 1.2) #Tamaño de la ventana
        self.size_win_y = int(self.h * 1)

        self.block_size_x = self.size_win_x/self.w
        self.block_size_y = self.size_win_y/self.h

        #Definicion de algunos colores
        self.red = (255, 0, 0)#Color meta
        self.green = (0, 255, 0)#Color inicio
        self.blue = (0, 0, 255)#Color visitados
        self.darkBlue = (0, 0, 128)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.purple = (163, 73, 164)#Ubicación
        self.orange = (253, 106, 2)#Color ruta
        self.gray = (192, 192, 192)
        
        #FUente para texto
        self.myfont = pygame.font.SysFont('Comic Sans MS', 25)

        #Se crea el canvas
        self.screen = pygame.display.set_mode((int(self.size_win_x), int(self.size_win_y)))
        
        #Se pinta el canvas y se pone la imagen
        self.screen.fill(self.white)
        self.screen.blit(image, (0, 0))
        
        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)
        #Se itera para pintar el punto de inicio y fin
        for y in range(self.h):
            for x in range(self.w):
                if self.start == (y, x):    #Si es el punto de inicio, pintar de rojo
                    pygame.draw.circle(self.screen,self.red,self.start[::-1],5,width=0)
                    self.isPainted[y][x]=True
                if self.goal == (y, x): #Si es el punto de fin, pintar de verde
                    pygame.draw.circle(self.screen,self.green,self.goal[::-1],5,width=0)
                    self.isPainted[y][x]=True

        #Pintar posición actual
        self.posFig = pygame.draw.circle(self.screen,self.purple,self.start[::-1],3,width=0)         


        #Escribir los tag
        (i, j) = (self.w * 1.025, int(self.h / 4))
        tagH = self.myfont.render('April Tag actual:', True, self.black)
        self.screen.blit(tagH, (i, j))
        self.myfont = pygame.font.SysFont('Comic Sans MS', 50)
        (i, j) = (self.w * 1.025, int(self.h / 4))
        tag = self.myfont.render(self.tag, False, self.black)
        self.screen.blit(tag, (i, j + 30))
        pygame.display.update()

        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)
        (i, j) = (self.w * 1.025, int(self.h / 2))
        coinH = self.myfont.render('Monedas Actuales:', True, self.black)
        self.screen.blit(coinH, (i, j))
        self.myfont = pygame.font.SysFont('Comic Sans MS', 50)
        (i, j) = (self.w * 1.025, int(self.h / 2))
        coin = self.myfont.render(self.coin, False, self.black)
        self.screen.blit(coin, (i, j + 30))
        pygame.display.update()
        
    def updateAprilTag(self, newValue):
        '''
        Funcion para actualizar el valor del April Tag de pantalla
        '''
        self.tag = newValue
        (i, j) = (self.w * 1, int(self.h / 4))
        self.screen.fill(self.white,(i,j+30,50,50))  
        tag = self.myfont.render(self.tag, False, self.black)
        self.screen.blit(tag, (i, j + 30))
        pygame.display.update()

    def updateCoinCount(self, newValue):
        '''
        Funcion para actualizar el valor del April Tag de pantalla
        '''
        self.tag = newValue
        (i, j) = (self.w * 1, int(self.h / 2))
        self.screen.fill(self.white,(i,j+30,50,50))  
        tag = self.myfont.render(self.tag, False, self.black)
        self.screen.blit(tag, (i, j + 30))
        pygame.display.update()
  
    def updatePos(self,pos):
        '''
        Funcion para actualizar la posicion actual
        '''
        (X,Y) = self.posFig.center  #Se obtiene la coordenada anterior
        print("Ac Odom", X, Y);
        if (Y,X) == self.start: #Si es el comienzo, se pinta de rojo para no dañar la ubicación
            self.posFig = pygame.draw.circle(self.screen,self.red,self.start[::-1],5,width=0)
        else:   #Si no, se pinta la anterior ubicación de blanco
            self.posFig = pygame.draw.circle(self.screen,self.white,(X,Y),3,width=0)
        #Se pinta la ubicación actual
        self.posFig = pygame.draw.circle(self.screen,self.purple,pos,3,width=0)
        pygame.display.update()
        
    def nodosVisitados(self,pos):
        '''
        Funcion para pintar las casillas visitadas
        '''
        pygame.draw.circle(self.screen,self.blue,pos,2,width=0)

    def nodosRuta(self,pos):
        '''
        Funcion para pintar la ruta
        '''
        pygame.draw.circle(self.screen,self.orange,pos,2,width=0)
        


if __name__ == '__main__':
    pygame.init()
    print 'SENECABOT GRUPO 4'
    rospy.init_node('GUI_node')
    print '==============================='
    cv2manager = cv2manager(PATHPLANO)
    puntos = cv2manager.seleccionarPuntos()
    gridmap = cv2manager.img / 255
    is_running = True
    print("Se iniciara la interfaz")
    pointsService = servicioPuntos(puntos)
    guiManager = GUI_manager(cv2manager.shape, puntos)
    aprilTagManager = aprilTag(guiManager)
    coinManager = contador_monedas(guiManager)
    visitadosManager = nodosVisitado(guiManager)
    nodosRuta = nodosRuta(guiManager)
    ubiacionManager = ubicaion(guiManager,puntos[0])
    while is_running:
        pygame.display.update()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                is_running = False
                pygame.quit()