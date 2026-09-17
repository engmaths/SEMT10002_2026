# =============================================================================
# Exercise 1 - Storing information about a robot
# =============================================================================
#
# Over the duration of this course, we're going to build a piece of code that
# can simulate the behaviour of a two-wheeled mobile robot. You can find out
# more about this model of robot at:
#   https://www.pololu.com/category/202/romi-chassis-and-accessories
#
# The first step in building this code is storing some information about the
# robot.
#
# The robot has two wheels separated by a distance (5.906 inches). Each wheel
# has a radius (1.378 inches) and turns at an angular speed, omega. The robot
# itself has a radius of 3.248 inches.
#
# We'll need to keep track of the robot's centre point (x, y) and orientation
# theta, measured clockwise from the y-axis.
#
# Create some variables to store this data in a Python script. Your code should
# convert any information given in inches to metric units - don't do this by
# hand! You should store the following pieces of data:
#
#   - The robot's name (your choice).
#   - The robot's radius in millimetres.
#   - The distance between the robot's two wheels in millimetres.
#   - The robot's current position and orientation (x = 0 mm, y = 0 mm,
#     theta = 0 rad).
#   - The radius of the robot's wheels in millimetres.
#
# Call your file "robot.py" and save it somewhere you'll remember, as we'll
# return to this file in later weeks.
# =============================================================================

# The measurements below are given in inches (as in the task description).
# Convert them to millimetres in your code -- 1 inch = 25.4 mm.
# Don't do the conversion by hand!

wheel_separation_in = 5.906   # distance between the two wheels
wheel_radius_in     = 1.378   # radius of each wheel
robot_radius_in     = 3.248   # radius of the robot body

# Your code here:
#   - give the robot a name
#   - store the robot radius, wheel separation and wheel radius in millimetres
#   - store the current position and orientation (x = 0 mm, y = 0 mm,
#     theta = 0 rad)
