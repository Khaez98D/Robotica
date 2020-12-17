#!/usr/bin/env python
# coding: latin-1

import cv2;
import rospy;
import apriltag;
from std_msgs.msg import String;
from sensor_msgs.msg import Image;
from cv_bridge import CvBridge, CvBridgeError;


tagID = "-";

def getImage(data):
	global tagID;
	try:
		bridge = CvBridge();
		frame = bridge.imgmsg_to_cv2(data, "bgr8");
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
	except CvBridgeError as e:
		raise;

	detector = apriltag.Detector();
	res = detector.detect(frame);

	if(res):
		tagID = str(res[0][1]);
	else:
		tagID = "-";


def pubAprilTags():
	pub = rospy.Publisher('/senecabot_tag', String, queue_size=30);
	sub = rospy.Subscriber("/camera_image", Image, getImage)
	rospy.init_node('senecabot_apriltags');
	rate = rospy.Rate(15);

	while not rospy.is_shutdown():
		global tagID;
		pub.publish(tagID);
		rate.sleep();


if __name__ == '__main__':
	try:
		pubAprilTags();
	except Exception as e:
		raise;