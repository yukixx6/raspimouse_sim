#!/usr/bin/env python
import rospy
from raspimouse_ros.msg import MotorFreqs

if __name__ == "__main__":
	rospy.init_node('motors_freq')
	pub = rospy.Publisher('motor_raw', MotorFreqs, queue_size=10)
	freq = MotorFreqs()
	try:
		while not rospy.is_shutdown():
			direction1 = raw_input('LeftMotor_freq > ')
			direction2 = raw_input('RightMotor_freq > ')

			if direction1.isdigit():
				#int(direction1)
				freq.left = int(direction1)

			else:
				rospy.logerr("cannot write to LeftMotor_freq")
			
			if direction2.isdigit():
				#int(direction2)
				freq.right = int(direction2)
			else:
				rospy.logerr("cannnot write to RightMotor_freq")

			print freq
			print "\n"
			pub.publish(freq)

	except rospy.ROSInterruptException:
		pass
