'''
## Exercise 5 - Storing information about a robot

The images here (https://github.com/engmaths/SEMT10002_2025/blob/main/media/week_1/romi.jpg) and
https://github.com/engmaths/SEMT10002_2025/blob/main/media/week_1/robot_kinematics_2.png
show a robot and a diagram labelling key parameters.  
You can find more about this model of robot [here](https://www.pololu.com/category/202/romi-chassis-and-accessories).

The robot has two wheels separated by a distance D. Each wheel has a radius r and turns at angular speed, omega.  
The centre point of the robot is at co-ordinates (x, y) and has orientation, theta, measured clockwise from the y-axis

To start with, we'll store some information about our robot. In particular, i'd like to store: 

+ The robot's name (your choice).
+ The robot's size (let's assume a circle of radius 160 mm).
+ The distance between two robot's wheels (150 mm).
+ The robot's current position and orientation (x= 0 mm, y= 0 mm, theta= 0 rad).
+ The radius of the robot's wheels (35 mm).

Create some variables to store this data in a Python script. 
Call your file "robot.py" and save it somewhere you'll remember as we'll return to this file in later weeks.

Suppose the robot moves for period `delta_t` with left wheel turning at angular speed, (omega) `ang_speed_left` and right wheel at angular speed (omega) `ang_speed_right`.
Both speeds are in radians per second.  The robot will either follow an arc of a circle or turn on the spot.  
Write some code to calculate the angle through which the robot turns during this move.
'''

#Put your code here.