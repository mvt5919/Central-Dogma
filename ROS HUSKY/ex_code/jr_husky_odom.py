
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
move_cmd = Twist()
move_cmd.linear.x = 0.2
move_cmd.angular.z = 0
move_tolerance = 0.01

# stop moving
stop_cmd = Twist()
stop_cmd.linear.x = 0
stop_cmd.angular.z = 0

# define the turning rate in rad/s 
turn_cmd = Twist()
turn_cmd.linear.x = 0
turn_cmd.angular.z = np.radians(30)
turn_tolerance = np.radians(5)
		
# define the publisher to publish commands
p = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
rospy.sleep(1.0)
		
def odom_lookup():
	listener = tf.TransformListener()
	rospy.sleep(0.2)

	# look up the odometry information
	try:
		((x,y,z), rot) = listener.lookupTransform('odom', 'base_link', rospy.Time(0))

	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		rospy.logger('Didnt work')

	# transforms the orientation from quaternion to euler so we can use data
	(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)

	return x, y, theta


def move(x, y):
	
	# define starting values 
	x_start = x
	y_start = y
	distance = 0
	
	while distance + move_tolerance <= length:

		# move forward at the speed defined above
		p.publish(move_cmd)
		rospy.loginfo('moving forward')
		
		# get the latest odometry information
		x, y, theta = odom_lookup()
			
		# calculate the distance traveled
		distance = np.sqrt(pow(x - x_start, 2) + pow(y - y_start, 2))
			
		print distance
		
	return x, y, theta	
		
def stop():

	# stop for 2 seconds to give the robot time to finish moving before turning. reduces error	
	p.publish(stop_cmd)
	print 'Stopping'
	rospy.sleep(2)
		

def turn(theta):

	# define starting angle
	angle_start = theta

	while abs(theta - angle_start) + turn_tolerance <= turn_angle:
			
		# turn at the speed defined above
		p.publish(turn_cmd)
		rospy.loginfo('turning')

		x, y, theta = odom_lookup()

		print abs(theta - angle_start)

	return x, y, theta

if __name__ == '__main__':
	
	rospy.init_node('odom_sub')
	try:
		
		x, y, theta = odom_lookup()
		x, y, theta = move(x, y)
		stop()
		x, y, theta = turn(theta)
		stop()
		x, y, theta = move(x, y)
		stop()
		x, y, theta = turn(theta)
		stop()
		x, y, theta = move(x, y)
		stop()
		x, y, theta = turn(theta)
		stop()
		x, y, theta = move(x, y)
		stop()
		x, y, theta = turn(theta)
		stop()
		
	except:

		print 'node terminated'	
