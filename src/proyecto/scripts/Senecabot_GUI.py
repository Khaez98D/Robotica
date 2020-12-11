#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import rospy
import pygame
import os
import pygame
import matplotlib.pyplot as plt

# from proyecto.srv import *

from tools import Tools
from std_msgs.msg import Float32MultiArray, Float32
os.environ['SDL_AUDIODRIVER'] = 'dsp'
PATHPLANO = r'/home/robotica/catkin_ws/src/proyecto/docs/Plano.jpeg'  # Path a la imagen del plano
puntoInicial = []  # Coordenadas punto inicial
puntoFinal = []  # Coordenadas punto final
PROB_FREE = 0.3  # Probabilidad de libre (Para pintar el mapa)
PROB_OCC = 0.6  # Probabilidad de ocupado (Para pintar el mapa)


class servicioPuntos:

    '''
    Nodo que provee el servicio de informar los puntos iniciales y finales
    '''

    def handleResponse(self, req):
        '''
        Metodo que informa las coordeanadas
        '''

        resp = 'El punto inicial es: ' + str(self.puntos[0]) \
            + '\nEl punto final es: ' + str(self.puntos[1])
        return pointsResponse(resp)

    def __init__(self, puntos):
        '''
        Metodo que inicializa el servidor
        '''

        self.puntos = puntos
        s = rospy.Service('Coordenadas', points, self.handleResponse)
        print 'Listo para informar coordenadas inicial y final'


class planeacionRuta:

    '''
    Nodo que recibe las celdas de la planeacion de ruta
    '''

    def __init__(self, GUI):
        rospy.Subscriber('/senecabot_route', Float32MultiArray,
                         self.callbackRoute)
        rospy.Subscriber('/senecabot_visited', Float32MultiArray,
                         self.callbackRoute)
        self.GUI = GUI

 
    def callbackRoute(self, data):
        dataCoord = data.data
        coord = (dataCoord[1], dataCoord[0])
        GUI.draw_visited(coord)


class ubiacion:

    '''
    Nodo que grafica sobre el mapa la posicion actual del robot
    '''

    def __init__(self,GUI):



class aprilTag:

    '''
    Nodo para determinar el april tag
    '''

    def __init__(self, GUI):
        rospy.Subscriber('/senecabot_tag', Float32)
        self.GUI = GUI
        self.tag = -1

    def callbackTag(self, data):
        tag = data.data
        if tag != self.tag:
            self.GUI.updateAprilTag(str(tag))


class cv2manager:

    '''
    Clase para manejar todo lo relacionado con cv2
    '''

    def __init__(self, path):
        self.img = cv2.imread(PATHPLANO, 0)
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

        image = pygame.image.load(PATHPLANO)
        self.tag = '-1'
        (self.h, self.w) = shape
        (self.start, self.goal) = coords
        self.start = tuple(self.start)[::-1]
        self.goal = tuple(self.goal)[::-1]
        self.size_win_x = int(self.w * 1)
        self.size_win_y = int(self.h * 1)
        self.block_size_x = 1
        self.block_size_y = 1
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.darkBlue = (0, 0, 128)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.pink = (255, 200, 200)
        self.orange = (253, 106, 2)
        self.gray = (192, 192, 192)
        self.prob_free = PROB_FREE
        self.prob_occ = PROB_OCC
        self.myfont = pygame.font.SysFont('Comic Sans MS', 25)
        self.screen = pygame.display.set_mode((int(self.size_win_x
                * 1.2), int(self.size_win_y)))
        self.screen.fill(self.white)
        self.screen.blit(image, (0, 0))
        for y in range(self.h):
            for x in range(self.w):
                rect = pygame.Rect(x * self.block_size_x, y
                                   * self.block_size_y,
                                   self.block_size_x * 10,
                                   self.block_size_y * 10)
                if self.start == (y, x):
                    pygame.draw.rect(self.screen, self.red, rect, 0)
                if self.goal == (y, x):
                    pygame.draw.rect(self.screen, self.green, rect, 0)

        (i, j) = (self.w * 1, int(self.h / 4))
        tagH = self.myfont.render('April Tag actual:', True, self.black)
        self.screen.blit(tagH, (i, j))
        self.myfont = pygame.font.SysFont('Comic Sans MS', 50)


        (i, j) = (self.w * 1, int(self.h / 4))
        tag = self.myfont.render(self.tag, False, self.black)
        self.screen.blit(tag, (i, j + 30))
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

    
    def updatePos(self,pos):
        '''
        Funcion para actualizar la posicion actual
        '''

    def nodosVisitados(self,pos):
        '''
        Funcion para pintar las casillas visitadas
        '''

    def nodosRuta(self,pos):
        '''
        Funcion para pintar la ruta
        '''


if __name__ == '__main__':
    print 'SENECABOT GRUPO 4'
    rospy.init_node('GUI_node')
    print '==============================='
    cv2manager = cv2manager(PATHPLANO)
    puntos = cv2manager.seleccionarPuntos()
    gridmap = cv2manager.img / 255
    is_running = True
    pygame.init()
    c = 12
    guiManager = GUI_manager(cv2manager.shape, puntos)
    aprilTagManager = aprilTag(guiManager)
    while is_running:
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                is_running = False
                pygame.quit()
