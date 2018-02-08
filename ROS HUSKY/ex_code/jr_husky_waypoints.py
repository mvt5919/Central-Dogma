
#! /usr/bin/env python

#########################################################################################
#
#
# File name: husky_waypoints.py
#
# Input waypoints and have husky turn to face and move toward input points
#
# Created: 01/26/18
#	- Jacob Randall
#	- jacobtrueno86@gmail.com
#
# Modified: 
#	01/26/18
#
# TODO:
#	- ***
# 
#########################################################################################

import rospy
import tf
import numpy as np 
from geometry_msgs.msg import Twist, Point 
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from husky_PID import PID
import angles

# Set my gains for PID controller
kp = 1.50
kd = 0.10
ki = 0.0

class waypoints(object):

	def __init__(self):

		# Call PID function from husky_PID.py.
		self.pid = PID(kp, ki, kd, 0.1, 100, -100, 0.0)

		# Call the angles script.
		self.ang = angles

		# Set a threshold for values to fall below.
		# Could set different thresholds for different function like moving forward distance
		# vs velocity but this threshold is good enough for everything in this script.
		self.threshold = 0.01

		# Create a command to move forward. Leave at 0 for now. Will be updated further on.
		self.move_cmd = Twist()

		# Create a command to turn.
		self.turn_cmd = Twist()

		# Create a publisher to the cmd_vel topic with message type of Twist.
		self.p = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
		rospy.sleep(0.5)

		# Create subscriber to subscribe to odom topic.
		self.listener = tf.TransformListener()
		rospy.sleep(0.5)

		# Define waypoints for husky to move to.
		self.targets = [[7, -2], [-8, -3], [1, 7], [2, -4], [-7, 1], [-1, 6], [0, 0]]

		# Define current goal point.
		self.current_goal = Point()

		# Define number of waypoints.
		self.length = len(self.targets)

	# Defining function to lookup odometry information.
	def odom_lookup(self):

		# Look up the position odometry information.
		try:
			((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_link', rospy.Time(0))
			

		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			print 'Position didnt work'

		# Transforms the orientation from quaternion to euler so we can use data.
		(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)
		
		# Look up the velocity odometry information.
		try:
			((v_x, v_y, v_z), (w_x, w_y, w_z)) = self.listener.lookupTwist('odom', 'base_link', rospy.Time(0), rospy.Duration(0.01))

		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			print 'Velocity didnt work'
		
		# Calculate resultant velocity from x and y vectors.
		self.velocity = np.sqrt(v_x**2 + v_y**2)
		
		# Set omega equal to the rotational speed around the z axis.
		self.omega = w_z

		# Return these values.
		return x, y, theta, self.velocity, self.omega

	def move(self, x, y, velocity):

		# Define starting point before moving.
		x_start = x
		y_start = y
		self.current_distance = 0.0
		
		# Setting last_state to 0 for the compute_output function.
		self.last_state = 0

		# Calculate the distance to goal.
		self.distance_to_goal = np.sqrt((self.current_goal.x - x_start)**2 + (self.current_goal.y - y_start)**2)
		
		# While it is not close enough to the goal or 
		# slow enough to stop accurately, keep moving.
		while abs(self.distance_to_goal - self.current_distance) >= self.threshold or velocity >= self.threshold:
			
			# Publish move_cmd to cmd_vel.
			self.p.publish(self.move_cmd)
			rospy.loginfo('Moving Forward')
			
			# Get latest and greatest odometry information.
			x, y, theta, velocity, omega = self.odom_lookup()

			# Calculate current distance from start point.
			self.current_distance = np.sqrt((x - x_start)**2 + (y - y_start)**2)

			# Calculate output by calling function from husky_PID.
			self.output = self.pid.compute_output(self.last_state, self.distance_to_goal, self.current_distance, None, None)
			
			# Update the last state for husky_PID.py script to properly calculate state_change.
			self.last_state = self.current_distance
			
			# Set the published command to the calculated output.
			self.move_cmd.linear.x = self.output

			print self.output

		return x, y, theta

	def turn(self, x, y, theta, omega):

		# Define starting angle.
		self.angle_start = theta
		
		self.last_state = 0
		
		# Calculate the x and y distances from facing to direction to direction of goal.
		int_y = self.current_goal.y - y
		int_x = self.current_goal.x - x
		
		# Calculate the angle needed to turn to point toward goal.
		self.angle_to_goal = np.arctan2(int_y, int_x)
		
		# Calculate the shortest angle to turn by calling function from angles.py.
		self.shortest_turn = self.ang.shortest_angular_distance(theta, self.angle_to_goal)
		
		while abs(self.shortest_turn) >= self.threshold or omega >= self.threshold:
			
			# Publish the turn_cmd to cmd_vel.
			self.p.publish(self.turn_cmd)
			rospy.loginfo('Turning')

			# Look up latest and greatest odometry information.
			x, y, theta, velocity, omega = self.odom_lookup()

			# Compute new shortest turn
			self.shortest_turn = self.ang.shortest_angular_distance(theta, self.angle_to_goal)

			# Current state
			self.current_state = self.angle_to_goal - self.shortest_turn

			# Calculate the desired output.
			self.output = self.pid.compute_output(self.last_state, self.angle_to_goal, self.current_state, None, None)

			# Update the last state for husky_PID.py script to properly calculate state_change.
			self.last_state = self.current_state

			# Set the published command to the calculated output.
			self.turn_cmd.angular.z = self.output

			"""print 'theta', theta

			print 'shortest turn', self.shortest_turn

			print 'angle to goal', self.angle_to_goal

			print 'current state', self.current_state

			print 'error', self.pid.error

			print 'state change', self.pid.state_change

			print 'output', self.output"""

		return x, y, theta

if __name__ == '__main__':

	# Initialize the node.
	rospy.init_node('go_to_waypoints')

	wp = waypoints()

	try:

		for i in range(0, wp.length):

			wp.current_goal.x = wp.targets[i][0]
			
			wp.current_goal.y = wp.targets[i][1]

			x, y, theta, velocity, omega = wp.odom_lookup()

			angle_to_goal = np.arctan2(wp.current_goal.y - y, wp.current_goal.x - x)
			
			if abs(angle_to_goal - theta) > wp.threshold:

				x, y, theta = wp.turn(x, y, theta, omega)
			
				x, y, theta = wp.move(x, y, velocity)
			
			else:

				x, y, theta, velocity, omega = wp.odom_lookup()

				x, y, theta = wp.move(x, y, velocity)

	except:

		print 'node terminated'	