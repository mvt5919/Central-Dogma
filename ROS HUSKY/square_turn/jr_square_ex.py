#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import radians
import time

def DrawAHexagon():

	rospy.init_node('drawahexagon')
	pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size = 10)
	r = rospy.Rate(5)
	
	move_cmd = Twist()
	move_cmd.linear.x = .5

	stop_cmd = Twist()
	stop_cmd.linear.x = 0

	turn_cmd = Twist()
	turn_cmd.angular.z = radians(28.125)

	while not rospy.is_shutdown():

		distance = 0
		speed = .5
		length = 1
		t0 = time.time()

		while distance < length:
			pub.publish(move_cmd)
			t1 = time.time()
			distance = speed * (t1-t0)
			r.sleep()

		t0 = time.time()
	
		while (t1-t0) < 1:
			pub.publish(stop_cmd)
			t1 = time.time()
			r.sleep()

		t0 = time.time()

		while (t1-t0) < 2:
			pub.publish(turn_cmd)
			t1 = time.time()
			r.sleep()

		t0 = time.time()

		while (t1-t0) < 1:
			pub.publish(stop_cmd)
			t1 = time.time()
			r.sleep()

if __name__ == '__main__':
	try:
		DrawAHexagon()
	except:
		print("node terminated")
