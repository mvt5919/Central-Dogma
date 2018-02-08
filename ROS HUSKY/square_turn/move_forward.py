#! /usr/bin/env python

#########################################################################################
#
#
# File name: move_forward.py
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

move_cmd = Twist()
move_cmd.linear.x = 0.2

p = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
rospy.sleep(0.5)
rospy.init_node('moving')

def move():

	while not rospy.is_shutdown():

		p.publish(move_cmd)

if __name__ == '__main__':

	move()


