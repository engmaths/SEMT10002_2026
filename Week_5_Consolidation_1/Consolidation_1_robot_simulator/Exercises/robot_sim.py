from robot_plotter import init_plot, snapshot, show_plot
from math import sin, cos, atan2, sqrt
from random import random

# constants about the robot
robot_name = "Daneel"
robot_radius = 160
wheel_separation = 150
robot_wheel_radius = 35

# initial robot configuration
robot_x_position = 500
robot_y_position = 500
robot_heading = 0

#Map information
map_x_min = 0
map_x_max = 5000
map_y_min  = 0
map_y_max = 5000
map_coords = ((map_x_min, map_x_max), (map_y_min, map_y_max))

# An obstacle with bottom left corner at at x = 100, y = 2250, width of 500 and height of 800.
obstacle_x = 100
obstacle_y = 2250
obstacle_width = 4000
obstacle_height = 500
obstacle = ((obstacle_x, obstacle_y), (obstacle_width, obstacle_height))
goal = (1000, 4000)

init_plot(robot_x_position,robot_y_position,robot_heading)

#This is the number of timesteps we simulate- change as is necessary.
num_steps = 100
#This is the default timestep - so by default we'll simulate 100 timesteps of 1 second= 100 seconds of movement. 
delta_t= 1 

for ii in range(num_steps):

    #Random() will give us a random number between 0 and 1, so these lines will set the wheel speeds to be random numbers between 0 and 5.
    ang_speed_left = 5 * random()
    ang_speed_right = 5 * random()

    # convert angular speeds into linear speeds with linear_velocity = angular_velocity * radius
    linear_speed_left = ang_speed_left * robot_wheel_radius
    linear_speed_right = ang_speed_right * robot_wheel_radius
    # angular speed of the robot is given by the difference in speeds divided by wheel spacing
    ang_speed_robot = (linear_speed_left - linear_speed_right) / wheel_separation
    # multiply angular speed by time to get the amount the angle has changed.
    angle_change = ang_speed_robot * delta_t
    ave_speed = 0.5*(linear_speed_left + linear_speed_right)

    # sinc
    if angle_change**2<0.01**2:
        the_sinc = 1-(0.25*angle_change*angle_change/6.0)
    else:
        the_sinc = sin(0.5*angle_change)/(0.5*angle_change)

    # update state
    robot_x_position = robot_x_position + ave_speed*delta_t*the_sinc*sin(robot_heading + 0.5*angle_change)
    robot_y_position = robot_y_position + ave_speed*delta_t*the_sinc*cos(robot_heading + 0.5*angle_change)
    robot_heading = robot_heading + angle_change

    print("X position: ", robot_x_position, ", Y position:", robot_y_position, ", Heading: ", robot_heading)
    snapshot(robot_x_position,robot_y_position,robot_heading)

    show_plot(map_coords, goal=goal, obstacle=obstacle, pause=0.1)

show_plot(map_coords, goal=goal, obstacle=obstacle)

