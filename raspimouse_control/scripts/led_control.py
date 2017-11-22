#!/usr/bin/env python
import rospy
from raspimouse_ros_2.msg import LedValues

if __name__ == "__main__":
	rospy.init_node('led_control')
	pub = rospy.Publisher('/raspimouse_on_gazebo/leds', LedValues, queue_size=10)
	try:
		while not rospy.is_shutdown():
			vel = LedValues()
			print ("ex) LED0 > on")
			direction0 = raw_input(' LED0 > ')
			direction1 = raw_input(' LED1 > ')
			direction2 = raw_input(' LED2 > ')
			direction3 = raw_input(' LED3 > ')

			if 'on' in direction0 or '1' in direction0:
				vel.right_side = True
			elif 'off' in direction0 or '0' in direction0:
				vel.right_side = False
			else:
				rospy.logerr("cannot write LED0" + "\n")

			if 'on' in direction1 or '1' in direction1:
				vel.right_forward = True
			elif 'off' in direction1 or '0' in direction1:
				vel.right_forward = False
			else:
				rospy.logerr("cannot write LED1" + "\n")

			if 'on' in direction2 or '1' in direction2:
				vel.left_forward = True
			elif 'off' in direction2 or '0' in direction2:
				vel.left_forward = False
			else:
				rospy.logerr("cannot write LED2" + "\n")

			if 'on' in direction3 or '1' in direction3:
				vel.left_side = True
			elif 'off' in direction3 or '0' in direction3:
				vel.left_side = False
			else:
				rospy.logerr("cannot write LED0" + "\n")

			print vel
			print "\n"
			pub.publish(vel)

	except rospy.ROSInterruptException:
		pass
