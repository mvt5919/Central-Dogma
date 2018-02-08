#! /usr/bin/env python

#########################################################################################
#
#
# File name: r_controller_ex.py
#
# description
#
# Created: 02/4/18
#	- Michael Tonore
#	- C00281379@louisiana.edu
#
# Modified: 
#
#
# TODO:
#	- ***
# 
#########################################################################################

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import *
import numpy as np
import tf

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
rospy.sleep(1.0)

def get_rot():
	listener = tf.TransformListener()
	rospy.sleep(0.2)

	try:
		((x,y,z), rot) = listener.lookupTransform('odom', 'base_link', rospy.Time(0))

	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		rospy.logger('Didnt work')

	# transforms the orientation from quaternion to euler so we can use data
	(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)

	return x, y, theta



rospy.init_node ("speed_controller")
rospy.loginfo("speed controller node init")



speed = Twist()

r = rospy.Rate(4)


goal = Point ()
goal.x = 5
goal.y = 5

while not rospy.is_shutdown():
	get_rot(x) = x
	get_rot(y) = y
	inc_x = goal.x - x
	inc_y = goal.y - y

	angle_to_goal = np.arctan2 (inc_y, inc_x)
	rospy.loginfo(theta)

	if abs(angle_to_goal - theta) > 0.1:
		speed.linear.x = 0.0
		speed.angular.z = 0.3
		rospy.loginfo("Correcting angle.")
	else:
		speed.linear.x = 0.5
		speed.angular.z = 0.0
		rospy.loginfo("Forward Roll.")

	pub.publish(speed)
	r.sleep()