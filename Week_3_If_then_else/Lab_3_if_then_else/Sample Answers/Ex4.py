'''
## Exercise 4 - Fuzzy logic

We're creating a chatbot to discuss the results of a survey of 100 people.  
To make it feel more conversational, it will use phrases "a few people" and "many people" instead of saying exact numbers.  
This will be achieved using fuzzy logic.The figure at (https://raw.githubusercontent.com/engmaths/SEMT10002_2025/refs/heads/main/media/week_2/fuzzy.png) shows
two _membership functions_ for fuzzy sets labeled "a few" and "many".  
Given a value, the code should calculate both membership functions, and return the label for the set with the highest value of its membership function.

- The function for "a few" is one for values of 5 or smaller (can count on one hand), zero for values of 12 or higher (a dozen) and linear in between.
- The function for "many" is zero for values of 9 or smaller (single figures), one for values of 50 or higher (more than half) and linear in between.

Example: for value 40, the function for "a few" is zero and the function for "many" is about 0.75.  The returned label is "many".

Write some code that takes a value and returns the label "a few" or "many" using the fuzzy logic above.
Also return "none" for the case of zero and show a message for any values that do not make sense.
'''

from math import sin, cos
from robot_plotter import init_plot,snapshot,show_plot

# constants about the robot
robot_name = "Daneel"
robot_radius = 160
wheel_separation = 150
robot_wheel_radius = 35

# initial robot configuration
robot_x_position = 0
robot_y_position = 0
robot_heading = 0

init_plot(0,0,0)

for ii in range(5):

    for jj in range(22):
        # variables to represent the wheel speed commands and duration of movement
        if jj==0:
            ang_speed_left = 1
            ang_speed_right = 0
            delta_t = 13.464
        elif jj==11:
            ang_speed_left = 0
            ang_speed_right = 1
            delta_t = 13.464
        else:
            ang_speed_left = 1
            ang_speed_right = 1
            delta_t = 2

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

        print(robot_x_position,robot_y_position,robot_heading)
        snapshot(robot_x_position,robot_y_position,robot_heading)

show_plot()