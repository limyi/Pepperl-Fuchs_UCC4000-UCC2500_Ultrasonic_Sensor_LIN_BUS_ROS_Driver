# Pepperl-Fuchs_UCC4000-UCC2500_Ultrasonic_Sensor_LIN_BUS_ROS_Driver
Serial Connection to LIN BUS Breakout Board to UCC4000 / UCC2500 Pepperl+Fuchs Ultrasonic Sensor

cd ~/catkin_ws/src

copy paste ultrasonic_sensors package into /catkin_ws/src

cd /ultrasonic_sensors/src

sudo chmod +x *

cd && cd catkin_ws

catkin_make

source devel/setup.bash

rosrun ultrasonic_sensors ultrasonic_main.py
