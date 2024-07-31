# Pepperl+Fuchs UCC4000 / UCC2500 Ultrasonic Sensor LIN BUS ROS Driver

## Overview
This guide provides instructions to connect the Pepperl+Fuchs UCC4000 / UCC2500 Ultrasonic Sensor via LIN BUS and run it using a ROS driver.

**Note:** Ensure that PWM mode is off for LIN BUS connection.

## Setup Instructions

1. **Clone the Repository**
    ```bash
    cd ~/catkin_ws/src
    ```

2. **Copy and Paste the `ultrasonic_sensors` Package**
    Copy the `ultrasonic_sensors` package into `/catkin_ws/src`.

3. **Make Scripts Executable**
    ```bash
    cd ~/catkin_ws/src/ultrasonic_sensors/src
    sudo chmod +x *
    ```

4. **Build the Catkin Workspace**
    ```bash
    cd ~/catkin_ws
    catkin_make
    ```

5. **Source the Setup Script**
    ```bash
    source devel/setup.bash
    ```

6. **Run the ROS Node**
    ```bash
    rosrun ultrasonic_sensors ultrasonic_main.py
    ```
