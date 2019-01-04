#! /usr/bin/env morseexec

from morse.builder import *
from airship_keyboard.builder.robots import Airship

# Add the MORSE mascott, MORSY.
# Out-the-box available robots are listed here:
# http://www.openrobots.org/morse/doc/stable/components_library.html
#
# 'morse add robot <name> air_ship_simulation' can help you to build custom robots.
robot = Airship()

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
robot.translate(2.0, 2.0, 2.0)
robot.rotate(0.0, 0.0, 3.5)

# Add a motion controller
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
#
# 'morse add actuator <name> air_ship_simulation' can help you with the creation of a custom
# actuator.
motion = MotionVW()
robot.append(motion)


# Add a keyboard controller to move the robot with arrow keys.
keyboard = Keyboard()
robot.append(keyboard)
keyboard.properties(ControlType = 'Position')

# Add a pose sensor that exports the current location and orientation
# of the robot in the world frame
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#sensors
#
# 'morse add sensor <name> air_ship_simulation' can help you with the creation of a custom
# sensor.

##########################################################################################
#Defining airship IMU
##########################################################################################

# creates a new instance of the sensor
imu = IMU()

# place your component at the correct location
imu.translate(0, 0, 0)
imu.rotate(0, 0, 0)

robot.append(imu)

# define one or several communication interface, like 'socket'
imu.add_interface('ros', topic="raw/imu")


##########################################################################################
#Defining airship camera
##########################################################################################
videocamera = VideoCamera()

videocamera.properties(cam_width=1280, cam_height=720, cam_focal=50)

# place your component at the correct location
videocamera.translate(0.4, 0., 0.)
videocamera.rotate(0., -1.6, 0.)

robot.append(videocamera)

# define one or several communication interface, like 'socket'
videocamera.add_interface('ros', topic="raw/cam")


##########################################################################################
#Defining airship lidar
##########################################################################################

# creates a new instance of the sensor
laserscanner = SickLDMRS()

laserscanner.properties(Visible_arc = True)
laserscanner.properties(resolution = 1.0)
laserscanner.properties(scan_window = 1.0)
laserscanner.properties(laser_range = 4.0)
laserscanner.frequency(10.0)

# place your component at the correct location
laserscanner.translate(0.39, 0., 0.)
laserscanner.rotate(0., 1.6, 0.)

robot.append(laserscanner)

# define one or several communication interface, like 'socket'
laserscanner.add_interface('ros', topic="raw/lidar")




pose = Pose()
robot.append(pose)

# To ease development and debugging, we add a socket interface to our robot.
#
# Check here: http://www.openrobots.org/morse/doc/stable/user/integration.html 
# the other available interfaces (like ROS, YARP...)
robot.add_default_interface('socket')


# set 'fastmode' to True to switch to wireframe mode
env = Environment('airship_train/cam2', fastmode = False)
env.set_camera_location([40, -50, 20])
env.set_camera_rotation([1.09, 0, 0.8])

