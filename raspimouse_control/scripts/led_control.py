#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__ == "__main__":
	rospy.init_node('led_control')
	pub = rospy.Publisher('/raspimouse_on_gazebo/leds', String, queue_size=10)
	try:
		while not rospy.is_shutdown():
			cmd = String()
			cmd.data = [0,0,0,0]
			direction = raw_input('[ LED0 LED1 LED2 LED3 ] > ')

			if '1' in direction[0]:
				cmd.data[0] = 1
			elif '0' in direction[0]:
				cmd.data[0] = 0
			else:
				rospy.logerr("cannot write LED0" + "\n")

			if '1' in direction[1]:
				cmd.data[1] = 1
			elif '0' in direction[1]:
				cmd.data[1] = 0
			else:
				rospy.logerr("cannot write LED1" + "\n")

			if '1' in direction[2]:
				cmd.data[2] = 1
			elif '0' in direction[2]:
				cmd.data[2] = 0
			else:
				rospy.logerr("cannot write LED2" + "\n")

			if '1' in direction[3]:
				cmd.data[3] = 1
			elif '0' in direction[3]:
				cmd.data[3] = 0
			else:
				rospy.logerr("cannot write LED3" + "\n")

			cmd.data = str(cmd.data)
			print cmd
			print "\n"
			pub.publish(cmd)

	except rospy.ROSInterruptException:
		##rospy.logerr("cannot write")
		pass
