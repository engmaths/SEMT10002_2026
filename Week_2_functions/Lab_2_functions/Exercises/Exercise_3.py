# =============================================================
# Exercise 3 - Robot wheel kinematics
# =============================================================
#
# Over this course, we're going to build a movement simulator for a simple 2 wheeled robot. 
#
# Our robot moves by spinning its two wheels independently - this
# is called a *differential drive*. The small amount of theory you
# need:
#
#   - A wheel of radius r spinning at angular speed omega (radians
#     per second) drives the robot forward at speed v = r * omega
#     at that wheel.
#   - When both wheels spin at the same speed, the robot drives in
#     a straight line. When they differ, it turns.
#   - The robot's overall forward speed is the *average* of its two
#     wheel speeds.
#   - The robot's turn rate (radians per second) is
#     (v_right - v_left) / W, where W is the wheel separation.
#
# Recall from week 1 (robot.py) that our robot's wheels have radius
# 35.0 mm and are separated by 150.0 mm.
#
# Part 1: Write the function wheel_speed(omega, radius) that returns the linear
#   speed of a wheel, with a docstring. If radius is in mm, what
#   units will the speed be in?
#
# Part 2: Write the function robot_speed(omega_left, omega_right, radius) that
#   returns the robot's forward speed. It should *call* wheel_speed
#   - and the average function from Exercise 1.
#
# Part 3: Write the function robot_motion(omega_left, omega_right, radius,
#   separation) that returns TWO values: the forward speed and the
#   turn rate.
#
# Sanity checks:
#   Both wheels at 2.0 rad/s -> forward speed 70.0 mm/s, turn rate 0.
#   Left -2.0 rad/s, right +2.0 rad/s -> forward speed 0 (the robot
#     spins on the spot). What is the turn rate?
# =============================================================

#from Week 1, Exercise 1
wheel_separation_in = 5.906   # distance between the two wheels
wheel_radius_in     = 1.378   # radius of each wheel
robot_radius_in     = 3.248   # radius of the robot body

robot_name = "Robby"
robot_radius_mm = robot_radius_in * 25.4
wheel_separation_mm = wheel_separation_in * 25.4
wheel_radius_m  = wheel_radius_in * 25.4

x = 0
y = 0
theta = 0

print("Name: ", robot_name)
print("Radius: ", robot_radius_mm)
print("Wheel spacing: ", wheel_separation_mm)
print("x: ", x, "y: ", y, "theta: ", theta)

# from Exercise 1
def average(m, n):
    return 0.5 * (m + n)

# Your code here
