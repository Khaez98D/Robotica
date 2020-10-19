#!/usr/bin/env python3
from turtle_bot_4.srv import turtle_bot_player,turtle_bot_playerResponse
import rospy
import os

NOVALIDO='El archivo no existe'

def rutaArchivo(req):
    print('Se esta buscando el arhivo con nombre [%s]' %req.nombre)
    path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'results/%s.txt'%req.nombre)
    existe = os.path.isfile(path)
    if existe:
        return path
    else:
        return NOVALIDO

def turtle_bot_player_server():
    rospy.init_node('turtle_bot_player_server')
    s = rospy.Service('turtle_bot_player',turtle_bot_player,rutaArchivo)
    print('Se inicia el servicio')
    rospy.spin()
    
if __name__ == '__main__':
    turtle_bot_player_server()