#!/usr/bin/env python
import rospy
from std_msgs.msg import String

devfile = '/dev/rtled'

def leds_callback(cmd):
	try:
		
		with open(devfile + '0','w') as f:
			f.write(cmd.data[1] + "\n")
			##f.write(1 + "\n") if cmd.data[1] == 1 else f.write(0 + "\n")
		with open(devfile + '1','w') as f:
			f.write(cmd.data[4])
			##f.write(1 + "\n") if cmd.data[4] == 1 else f.write(0 + "\n")
		with open(devfile + '2','w') as f:
			f.write(cmd.data[7])
			##f.write(1 + "\n") if cmd.data[7] == 1 else f.write(0 + "\n")
		with open(devfile + '3','w') as f:
			f.write(cmd.data[10])
			##f.write(1 + "\n") if cmd.data[10] == 1 else f.write(0 + "\n")
		'''
		print cmd.data[1]
		print cmd.data[4]
		print cmd.data[7]
		print cmd.data[10]
		'''

	except:
		rospy.logerr("cannot write" + devfile + "[0,1,2,3]")

if __name__ == "__main__":
	rospy.init_node("led_data")
	rospy.Subscriber("/raspimouse_on_gazebo/leds", String, leds_callback)
	rospy.spin()
