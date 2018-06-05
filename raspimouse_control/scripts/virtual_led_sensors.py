#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import rospy, math
from sensor_msgs.msg import LaserScan
from raspimouse_ros.msg import LightSensorValues

def range_to_led(range_value):
    try:
        distance = int(range_value[0] * 1000)  # distance[mm]
        if distance < 4: distance = 8 - distance
        # This formula is calculated from the measurement result of actual sensor.
        # http://products.rt-net.jp/micromouse/archives/3361
        led_value = int(761000 / math.pow(distance, 1.66))
        if led_value > 4000: led_value = 4000
        if led_value < 15: led_value = 15
    except:
        led_value = 15
    return led_value


def write_to_file(data):
    try:
        with open("/dev/rtlightsensor0", "w") as f:
            print("%d %d %d %d" % tuple(data), file=f)
    except:
        rospy.logerr("failed to open rtlightsensor0")


def sensor1_callback(data):
    led_val[0] = range_to_led(data.ranges)


def sensor2_callback(data):
    led_val[1] = range_to_led(data.ranges)


def sensor3_callback(data):
    led_val[2] = range_to_led(data.ranges)


def sensor4_callback(data):
    led_val[3] = range_to_led(data.ranges)
    write_to_file(led_val)
    talker(led_val)

def listener():
    rospy.Subscriber(rospy.get_namespace() + "rf_scan", LaserScan, sensor1_callback)
    rospy.Subscriber(rospy.get_namespace() + "rs_scan", LaserScan, sensor2_callback)
    rospy.Subscriber(rospy.get_namespace() + "ls_scan", LaserScan, sensor3_callback)
    rospy.Subscriber(rospy.get_namespace() + "lf_scan", LaserScan, sensor4_callback)

def talker(data):
    #rospy.init_node('lightsensors')
    pub = rospy.Publisher('lightsensors', LightSensorValues, queue_size=1)
    try:
        # rospy.loginfo(sensor1.ranges[0] * 1000)
        d = LightSensorValues()
        d.right_forward = data[0]
        d.right_side = data[1]
        d.left_side = data[2]
        d.left_forward = data[3]
        pub.publish(d)
    except:
        rospy.logerr("Converting Sensor Data Failed")


if __name__ == "__main__":
    led_val = [15, 15, 15, 15]
    rospy.init_node("sensor_data_converter", anonymous=True)
    listener()
    rospy.spin()
