# robot simulation

'''
## Task

Write a program that generates a robot log file. 

Each time the program saves a snapshot of the robot, it should also record the following information and save it to log file:
- timestamp 
- position of the robot
- orientation of the robot
- the state information: "Collision with wall"/"Collision with obstacle" if the robot has 
collided with a wall or obstacle respectively, otherwise the state information should be blank (i.e. an empty string) 
'''

# Import modules
from robot_plotter import init_plot, snapshot, show_plot
from math import sin, cos, atan2, sqrt, pi
from random import random
from time import perf_counter
import csv

# constants about the robot
robot_name = "Daneel"
robot_radius = 160
# put any other constants you need here

# utility functions...
def func():
    # your code here
    '???' # <-- replace

# any more functions you need in here

# main simulation function
def main():
    # your code here
    '???' # <-- replace

# magic to run the main function if invoked as a script
if __name__=='__main__':
    main()