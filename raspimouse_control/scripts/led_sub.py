#!/usr/bin/env python
import rospy
from std_msgs.msg import String

devfile = '/dev/rtled'

def leds_callback(data):
	try:
		
		with open(devfile + '0','w') as f:
			f.write(data.data[1] + "\n")
		with open(devfile + '1','w') as f:
			f.write(data.data[4])
		with open(devfile + '2','w') as f:
			f.write(data.data[7])
		with open(devfile + '3','w') as f:
			f.write(data.data[10])
	except:
		rospy.logerr("cannot write" + devfile + "[0,1,2,3]")

if __name__ == "__main__":
	rospy.init_node("led_data")
	rospy.Subscriber("/raspimouse_on_gazebo/leds", String, leds_callback)
	rospy.spin()
