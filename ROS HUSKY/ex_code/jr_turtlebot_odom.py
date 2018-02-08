
#!/usr/bin/env python

import roslib
import rospy
import tf
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty

# define the side length
length = 1

# define the angle to turn in degrees converted to radians
turn_angle = np.radians(90)

# define the moving velocity in m/s
move = Twist()
move.linear.x = 0.2
move.angular.z = 0

# stop moving
stop = Twist()
stop.linear.x = 0
stop.angular.z = 0

# define the turning rate in rad/s 
turn = Twist()
turn.linear.x = 0
turn.angular.z = np.radians(30)

# pulls the latest common data from time
now = rospy.Time(0)

class draw_a_square:
	def __init__ (self):
		
		# if the node shuts down do the shutdwon function
		rospy.on_shutdown(self.shutdown)

		# create a variable for the listener
		self.listener = tf.TransformListener()

		# define the publisher to publish commands
		self.p = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size = 10)
		rospy.sleep(1.0)
		
		# look up the odometry information
		try:
			((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)

		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			rospy.logger('Didnt work')

		# transforms the orientation from quaternion to euler so we can use data
		(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)
		
		# define starting values 
		x_start = x
		y_start = y
		distance = 0

		while distance <= length:

			# move forward at the speed defined above
			self.p.publish(move)
			rospy.loginfo('moving forward')

			# get the latest odometry information
			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')
			
			# calculate the distance traveled
			distance = np.sqrt(pow(x - x_start, 2) + pow(y - y_start, 2))
			
			print distance
		
		# stop for 2 seconds to give the robot time to finish moving before turning. reduces error	
		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)

		# define starting angle
		angle_start = theta
		while abs(abs(theta) - angle_start) <= turn_angle:
			
			# turn at the speed defined above
			self.p.publish(turn)
			rospy.loginfo('turning')

			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')

			(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)

			print abs(abs(theta) - angle_start)

		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)

		x_start = x
		y_start = y
		distance = 0

		while distance <= length:	
			
			self.p.publish(move)
			rospy.loginfo('moving forward')
			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')

			distance = np.sqrt(pow(x - x_start, 2) + pow(y - y_start, 2))
			
			print distance
			
		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)

		angle_start = theta
		while abs(theta - angle_start) <= turn_angle:
			
			self.p.publish(turn)
			rospy.loginfo('turning')
			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')

			(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)

			print abs(theta - angle_start)
			print angle_start
			print theta

		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)

		x_start = x
		y_start = y
		distance = 0

		while distance <= length:	
			
			self.p.publish(move)
			rospy.loginfo('moving forward')
			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')
			
			distance = np.sqrt(pow(x - x_start, 2) + pow(y - y_start, 2))
			
			print distance
			
		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)
		
		angle_start = abs(theta)
		while abs(abs(theta) - angle_start) <= turn_angle:
			
			self.p.publish(turn)
			rospy.loginfo('turning')
			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')

			(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)
			
			print abs(theta - angle_start)
			print theta
			print angle_start
			

		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)

		x_start = x
		y_start = y
		distance = 0

		while distance <= length:	
			
			self.p.publish(move)
			rospy.loginfo('moving forward')
			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')
		
			distance = np.sqrt(pow(x - x_start, 2) + pow(y - y_start, 2))
			
			print distance
			
		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)

		angle_start = theta
		while abs(theta - angle_start) <= turn_angle:
			
			self.p.publish(turn)
			rospy.loginfo('turning')
			try:
				((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', now)
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				rospy.logger('Didnt work')

			(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)
			
			print abs(theta - angle_start)
			
		self.p.publish(stop)
		print 'Stopping'
		rospy.sleep(2)

	# if node shuts down stop moving
	def shutdown(self):
		rospy.loginfo("Stopping the robot...")
		self.p.publish(Twist())
		rospy.sleep(1)

if __name__ == '__main__':
	
	# initialize the node
	rospy.init_node('draw_a_square')
	try:
		draw_a_square()
	except:
		print 'node terminated'	
