'''
================
Exercise 5
================

We are going to update the robot program so that the robot has, not just one, but *multiple* obstacles to avoid. 

The library robot_plotter.py has been updated...

The function `show_plot(map_coords, goal=None, obstacle=None, pause=0)` had an optional argument `obstacle`, with format:
((obstacle_x, obstacle_y), (obstacle_width, obstacle_height))

Rather than plotting a single obstacle, the function can now plot any number of obstacles. 
To achieve this, the optional argument, `obstacle`, has been replaced by an optional argument `obstacles` which 
instead has the format of a list. Examples:


1 obstacle

[((obstacle_1_x, obstacle_1_y), (obstacle_1_width, obstacle_1_height))]


2 obstacles

[((obstacle_1_x, obstacle_1_y), (obstacle_1_width, obstacle_1_height)),
 ((obstacle_2_x, obstacle_2_y), (obstacle_2_width, obstacle_2_height))]


3 obstacles

[((obstacle_1_x, obstacle_1_y), (obstacle_1_width, obstacle_1_height)),
 ((obstacle_2_x, obstacle_2_y), (obstacle_2_width, obstacle_2_height)),
 ((obstacle_3_x, obstacle_3_y), (obstacle_3_width, obstacle_3_height))]


1. Copy your code from Consolidation Exercise 1, Task 2: Collision Avoidance. 

2. Update your programme so that any number of obstacles can be generated, and the robot detects and avoids all obstcles
'''
