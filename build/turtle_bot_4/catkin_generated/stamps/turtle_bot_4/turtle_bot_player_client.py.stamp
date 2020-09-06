#!/usr/bin/env python3
import sys,rospy,os
from turtle_bot_4.srv import *

NOVALIDO='El archivo no existe'


def turtle_bot_playerClient(rutaArchivo):
    x=[]
    rospy.wait_for_service('turtle_bot_player')
    try:
        ruta=rospy.ServiceProxy('turtle_bot_player',turtle_bot_player)
        response = ruta(nombreArchivo)
        if(response!=NOVALIDO):
            with open(str(response),mode='r') as reader:
                lines = reader.readlines()
                for line in lines:
                    x.append(lines)
            return x
        else:
            return 'ruta no valida'
    except rospy.ServiceException:
        print('Fallo llamado al servicio')

def usage():
    return 'xd'

if __name__=='__main__':
    print('Hola')
    print(sys.argv)
    if(len(sys.argv)==2):
        nombreArchivo = sys.argv[1]
    else:
        print("Aiuda")
        print(usage())
    print("Se hizo un request del servicio")
    print(turtle_bot_playerClient(nombreArchivo))
    
        