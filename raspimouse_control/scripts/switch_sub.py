#!/usr/bin/env python
import rospy
from raspimouse_ros.msg import Switches

devfile = '/dev/rtswitch'

def switches_callback(data):
	try:
		with open(devfile + '0','w') as f:
			f.write('0' + "\n") if data.front == True else f.write('1' + "\n")
		with open(devfile + '1','w') as f:
			f.write('0' + "\n") if data.center == True else f.write('1' + "\n")
		with open(devfile + '2','w') as f:
			f.write('0' + "\n") if data.rear == True else f.write('1' + "\n")
	except:
		rospy.logerr("cannot write" + devfile + "[0,1,2]")

if __name__ == "__main__":
	rospy.init_node("switches_data")
	rospy.Subscriber("/raspimouse_on_gazebo/switches", Switches, switches_callback)
	rospy.spin()
