#! /usr/bin/env python

#########################################################################################
#
#
# File name: r_controller_ex.py
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
#	- 
# 
#########################################################################################

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Point, Twist, Quaternion
from math import atan2

roll = 0.0
pitch = 0.0
yaw = 0.0

def get_rot (msg):
	global roll
	global pitch
	global yaw
	rot_q = msg.pose.pose.orientation
	rot_list = [rot_q.x, rot_q.y, rot_q.z, rot_q.w]
	(roll, pitch, yaw) = euler_from_quaternion (rot_list)
	print yaw
	#rospy.loginfo(yaw)

x = 0.0
y = 0.0

def get_pos (msg):
	global x
	global y

	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y

rospy.init_node ("speed_controller")
rospy.loginfo("speed controller node init")

sub = rospy.Subscriber("/odometry/filtered", Odometry, get_rot)
sub = rospy.Subscriber("/odometry/filtered", Odometry, get_pos)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
#rospy.loginfo(yaw)

speed = Twist()

r = rospy.Rate(4)


goal = Point ()
goal.x = 5
goal.y = 5

while not rospy.is_shutdown():
	quat = quaternion_from_euler (roll, pitch, yaw)
	print quat
	inc_x = goal.x - x
	inc_y = goal.y - y

	angle_to_goal = atan2 (inc_y, inc_x)
	rospy.loginfo(quat)

	if abs(angle_to_goal - quat[3]) > 0.1:
		speed.linear.x = 0.0
		speed.angular.z = 0.3
		rospy.loginfo("Correcting angle.")
	else:
		speed.linear.x = 0.5
		speed.angular.z = 0.0
		rospy.loginfo("Forward Roll.")

	pub.publish(speed)
	r.sleep()
