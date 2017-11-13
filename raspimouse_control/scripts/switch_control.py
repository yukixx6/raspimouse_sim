#!/usr/bin/env python
import rospy,sys
from raspimouse_ros.msg import Switches

if __name__ == '__main__':
	roapy.init_nade('switch_vel_pub')
	pub = rospyPublisher('/swiches', Switch, queue_size=1)
		try:
			while not rospy.is_shutdown():
				vel = Switches()
				direction0 = raw_input('SW0 > ')
				direction1 = raw_input('SW1 > ')
				direction2 = raw_input('SW2 > ')

				vel.front = True if '0' in direction0 else False
				vel.center = True if '0' in direction1 else False
				vel.rear = True if '0' in direction2 else False

				print vel
				pub.publish(vel)
			except:
				roapy.logerr("cannot write")
