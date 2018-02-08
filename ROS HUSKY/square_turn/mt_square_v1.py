#! /usr/bin/env python

#########################################################################################
#
#
# File name: mt_square_v1.py
#
# description
#
# Created: 02/1/18
#	- Michael Tonore
#	- C00281379@louisiana.edu
#
# Modified: 
#	02/1/18
#
# TODO:
#	- ***
# 
#########################################################################################

import rospy
from geometry_msgs.msg import Twist
from math import radians
import time

def DrawASquare():

	rospy.init_node('drawasquare')
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	r = rospy.Rate(5)
	
	move_cmd = Twist()
	move_cmd.linear.x = .5

	stop_cmd = Twist()
	stop_cmd.linear.x = 0

	turn_cmd = Twist()
	turn_cmd.angular.z = radians(45)

	while not rospy.is_shutdown():

		distance = 0
		speed = .5
		length = 1.3
		t0 = time.time()

		while distance < length:
			
			pub.publish(move_cmd)
			rospy.loginfo("Going Straight")
			t1 = time.time()
			distance = speed * (t1-t0)
			r.sleep()

		t0 = time.time()
	
		while (t1-t0) < 1:
			
			pub.publish(stop_cmd)
			rospy.loginfo("Stopping")
			t1 = time.time()
			r.sleep()

		t0 = time.time()

		while (t1-t0) < 2:
			
			pub.publish(turn_cmd)
			rospy.loginfo("Left Turn")			
			t1 = time.time()
			r.sleep()

		t0 = time.time()

		while (t1-t0) < 1:
			
			pub.publish(stop_cmd)
			rospy.loginfo("Stopping")			
			t1 = time.time()
			r.sleep()

if __name__ == '__main__':
	try:
		DrawASquare()
	except:
		rospy.loginfo("node terminated")
