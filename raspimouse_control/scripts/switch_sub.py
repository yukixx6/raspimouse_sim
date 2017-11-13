#!/usr/bin/env python
import sys, rospy
from raspimouse_ros.msg import Switches

def switches_callback():
		try:
			with open(devfile + '0','w') as f:
				'0' if vel.front == True else '1'
			with open(devfile + '1','w') as f:
				'0' if vel.center == True else '1'
			with open(devfile + '2','w') as f:
				'0' if vel.rear == True else '1'
		except:
			rospy.logerr("cannot write" + devfile + "[0,1,2]")

def listener():
	rospy.Subscriber("switches", Switches, switches_callback)

if __name__ == "__main__":
	vel = Switches()
	devfile = '/dev/rtswitch'
	rospy.init_node("switches_data")
	listener()
	print vel
	rospy.spin()

