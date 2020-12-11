#!/usr/bin/env python
import sys,rospy
from proyecto.srv import *
def cliente_puntos():
    rospy.wait_for_service('Coordenadas')
    try:
        server = rospy.ServiceProxy('Coordenadas',points)
        resp = server('ignorar')
        return resp.coords
    except rospy.ServiceException,e:
        print "Service_call_failed:_%s"%e
if __name__=="__main__":
    print "%s"%cliente_puntos()