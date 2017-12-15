#!/usr/bin/env python
import rospy, math
import subprocess
from geometry_msgs.msg import Twist

def motor_freq():
	swfile ='/dev/rtmotoren0'
	lfile = '/dev/rtmotor_raw_l0'
	rfile = '/dev/rtmotor_raw_r0'
	vel = Twist()
	count = 0

	while not rospy.is_shutdown():
		try:
			with open(swfile,'r') as f:
				if f.readline().rstrip()=='1':
					if count == 1:
						subprocess.call("aplay ~/catkin_ws/src/raspimouse_sim/raspimouse_control/scripts/decision3.wav", shell=True)
					with open(lfile,'r') as lf,\
						 open(rfile,'r') as rf:
						lhz_str = lf.readline().rstrip()
						rhz_str = rf.readline().rstrip()
						if len(lhz_str)!=0 and len(rhz_str)!=0:
							lhz = int(lhz_str)
							rhz = int(rhz_str)
							vel.linear.x = (lhz+rhz)*9*math.pi/160000.0
							vel.angular.z = (rhz-lhz)*math.pi/800.0
							print vel
							pub.publish(vel)
						
							count = 0
				else:
					if count == 0:
						rospy.logerr("not enpowered")
						count = 1
		except rospy.ROSInterruptException:
			pass

if __name__ == "__main__":
	rospy.init_node('virtual_motors')
	pub = rospy.Publisher('/raspimouse_on_gazebo/diff_drive_controller/cmd_vel', Twist, queue_size=10)
	motor_freq()
	rospy.spin()

