#!/usr/bin/env python

#### Created by SUTD ROAR LAB ####
@author: Lim Yi, Joel Chan, Yan Le Singaopore University of Technology and Design

import rospy
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist
import serial
import struct
import time
import sys
import linbus_ultrasonic as ultra

class RosHandler:

    def __init__(self):

        self.data_publisher = rospy.Publisher("/ultrasonic_data", Twist, queue_size=3)
        print("Running")
        self.ultrasonic_sensor = ultra.Ultrasonic('/dev/ttyUSB0') # Check serial port address

        self.distance = 0

    def run(self):

        while not rospy.is_shutdown():
            self.distance = self.ultrasonic_sensor.measure()
            data_array = Twist()

            data_array.linear.x = 0
            data_array.linear.y =0
            data_array.linear.z = self.distance
            data_array.angular.x = 0
            data_array.angular.y = 0
            data_array.angular.z = 0

            self.data_publisher.publish(data_array)
            rate.sleep()
        return 

if __name__ == '__main__':
    rospy.init_node('ultrasonic_sensor')
    rate = rospy.Rate(10) # 10hz
    rh = RosHandler()
    rh.run()
