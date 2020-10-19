#!/usr/bin/env python3
import sys,rospy,os,turtle_bot_teleop
from turtle_bot_4.srv import *
from pynput.keyboard import Controller,Key
from geometry_msgs.msg import Twist

NOVALIDO='El archivo no existe'
keys = {str(Key.up):Key.up,str(Key.down):Key.down,str(Key.left):Key.left,str(Key.right):Key.right}
msgLin,msgAng=0.0,0.0

def turtle_bot_playerClient(rutaArchivo):
    lines=[]
    rospy.wait_for_service('turtle_bot_player')
    ruta=rospy.ServiceProxy('turtle_bot_player',turtle_bot_player)
    response = ruta(nombreArchivo)
    try:
        with open(str(response.ruta),mode='r') as reader:
            lines = reader.readlines()
            for i in range(len(lines)):
                lines[i]=lines[i].replace('\n','')
        return lines
    except rospy.ServiceException:
        print('Fallo llamado al servicio')

def usage():
    return NOVALIDO


def replay(lineas,vLin,vAng):
    global msgLin
    global msgAng
    pub = rospy.Publisher('turtlebot_cmdVel', Twist, queue_size=10)
    rospy.init_node('turtle_bot_player')
    rate = rospy.Rate(50)
    i=0
    while not rospy.is_shutdown() and i<len(lineas):
        msg = Twist()
        actVel(lineas[i])
        msg.linear.x = msgLin*vLin
        msg.angular.z = msgAng*vAng
        pub.publish(msg)
        parar()
        i+=1
        rate.sleep()
    
def actVel(key):
    global msgLin
    global msgAng

    if key == str(Key.up):
        msgLin = 1
        msgAng = 0

    elif key == str(Key.down):
        msgLin = -1
        msgAng = 0

    elif key == str(Key.left):
        msgAng = 1
        msgLin = 0

    elif key == str(Key.right):
        msgAng = -1
        msgLin = 0
        
        
def parar():
    global msgLin
    global msgAng
    msgLin = 0.0
    msgAng = 0.0

if __name__=='__main__':
    if(len(sys.argv)==2):
        nombreArchivo = sys.argv[1]
    else:
        print("Aiuda")
        print(usage())
    print("Se hizo un request del servicio")
    lineas = turtle_bot_playerClient(nombreArchivo)
    velocidades = lineas[0].split(";")
    lineas.remove(lineas[0])
    replay(lineas,float(velocidades[1]),float(velocidades[2]))
    
        