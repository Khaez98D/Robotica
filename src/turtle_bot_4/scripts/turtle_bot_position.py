#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy;
import traceback;
import math;
from geometry_msgs.msg import Twist;
import matplotlib.pyplot as plt;

xPos = [0.0];
yPos = [0.0];

def recibido(msg):
    
    if msg.linear.x != xPos[-1] or msg.linear.y != yPos[-1]:
        xPos.append(msg.linear.x);
        yPos.append(msg.linear.y);
        actGraph();

def actGraph():
    plt.subplot(111);
    plt.clf();
    plt.axis([-2.5, 2.5, -2.5, 2.5]);
    plt.plot(xPos, yPos);
    plt.scatter(xPos[-1], yPos[-1], s=40);
    plt.pause(0.01);
    #plt.savefig("/home/robotica/catkin_ws/src/turtle_bot_4/results/trayectoria_punto2.png");


def turtlePos():
    rospy.init_node('turtle_bot_position');
    rospy.Subscriber('turtlebot_position', Twist, recibido);
    plt.show()
    rospy.spin();
    


if __name__ == '__main__':
    try:
        turtlePos();
    except Exception as e:
        print(traceback.format_exc());
