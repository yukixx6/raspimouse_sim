#!/usr/bin/env python
import rospy
from raspimouse_ros_2.msg import LedValues

devfile = '/dev/rtled'

def leds_callback(data):
	try:
		with open(devfile + '0','w') as f:
			f.write('1' + "\n") if data.right_side == True else f.write('0' + "\n")
		with open(devfile + '1','w') as f:
			f.write('1' + "\n") if data.right_forward == True else f.write('0' + "\n")
		with open(devfile + '2','w') as f:
			f.write('1' + "\n") if data.left_forward == True else f.write('0' + "\n")
		with open(devfile + '3','w') as f:
			f.write('1' + "\n") if data.left_side == True else f.write('0' + "\n")
	except:
		rospy.logerr("cannot write" + devfile + "[0,1,2,3]")

if __name__ == "__main__":
	rospy.init_node("led_data")
	rospy.Subscriber("/raspimouse_on_gazebo/leds", LedValues, leds_callback)
	rospy.spin()
