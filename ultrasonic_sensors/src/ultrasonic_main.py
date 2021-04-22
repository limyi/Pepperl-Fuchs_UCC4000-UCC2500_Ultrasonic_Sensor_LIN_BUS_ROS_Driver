#!/usr/bin/env python3

#### Created by SUTD ROAR LAB ####

import rospy
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist
import serial
import struct
import time
import sys
import linbus_ultrasonic as ultra
from bitarray import bitarray # pip install bitarray
import bitarray.util as util
from binascii import hexlify

class RosHandler:

    def __init__(self):

        self.data_publisher = rospy.Publisher("/ultrasonic_data", Twist, queue_size=3)
        print("Running")
        self.ultrasonic_sensor1 = ultra.Ultrasonic('/dev/ttyUSB2',debug=True, address=1) # Check serial port address
        self.ultrasonic_sensor2 = ultra.Ultrasonic('/dev/ttyUSB3',debug=True, address=1)
        self.distance1 = 0
        self.distance2 = 0

    def run(self):

        while not rospy.is_shutdown():
            #self.distance = self.ultrasonic_sensor._checksum([167,54,85])
            self.distance1 = self.ultrasonic_sensor1.measure()
            self.distance2 = self.ultrasonic_sensor2.measure()
            #print(self.distance) # 115
            print("distance1 :", self.distance1)
            print("distance2: ", self.distance2)
            data_array = Twist()

            data_array.linear.x = self.distance1
            data_array.linear.y = self.distance2
            data_array.linear.z = 0
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
