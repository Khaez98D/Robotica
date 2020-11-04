#!/usr/bin/env python
import sys,rospy,os
import time
import numpy as np
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray,Float32,String
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion



def takler():
    pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x=1
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=0
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()



def callback(data):
    print("-------------------------------------------------------------------------------")
    pose = data.pose.pose
    rospy.loginfo(pose.position)
    rospy.loginfo(euler_from_quaternion([pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w]))


def listener():
    rospy.init_node('Listener',anonymous=True)
    rospy.Subscriber('odom',Odometry,callback)
    rospy.spin()


if __name__=='__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass