#!/usr/bin/env python
#coding:utf-8
import rospy, math
from geometry_msgs.msg import Twist


def motor_freq():
	lfile = '/dev/rtmotor_raw_l0'
	rfile = '/dev/rtmotor_raw_r0'
	vel = Twist()

	while not rospy.is_shutdown():
		try:
			with open(lfile,'r') as lf,\
			open(rfile,'r') as rf:
				lhz_str = lf.readline().rstrip()
				rhz_str = rf.readline().rstrip()
				if len(lhz_str)!=0 and len(rhz_str)!=0:

					#rhz = int(rf.readline().rstrip())
					#lhz = int(lf.readline().rstrip())

					lhz = int(lhz_str)
					rhz = int(rhz_str)
					##print (lhz_str,rhz_str)
					##lhz = float(lf.readline())
					##rhz = float(rf.readline())\
					vel.linear.x = (lhz+rhz)*9*math.pi/160000.0
					vel.angular.z = (rhz-lhz)*math.pi/800.0
				
					print vel
					pub.publish(vel)
				else:
					print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
					#rospy.logerr("cannot")
		except rospy.ROSInterruptException:
			pass

if __name__ == "__main__":
	rospy.init_node('virtual_motors')
	pub = rospy.Publisher('/raspimouse_on_gazebo/diff_drive_controller/cmd_vel', Twist, queue_size=10)
	motor_freq()
	rospy.spin()


