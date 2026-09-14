# simple plotting utility for 2D robot simulator

from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Scaler for plotting robot
robot_size = 50

# Define triangle shape for robot
robot_shape = robot_size*np.array([[-1,0,1,-1],
                                  [-1,1,-1,-1]])

# Variables to store the history of robot positions and headings
x_log = []
y_log = []
th_log = []

def init_plot(x_position,y_position,heading):
    """
    Clears the log of x and y position and heading (theta) of the robot
    Then stores the current x and y position and heading (theta) of the 
    robot to the log
    """
    x_log.clear()
    y_log.clear()
    th_log.clear()
    snapshot(x_position,y_position,heading)

def snapshot(x_position,y_position,heading):
    """
    Stores the current x and y position and heading (theta) of the robot
    to a log
    """
    x_log.append(x_position)
    y_log.append(y_position)
    th_log.append(heading)

def rotation_matrix(theta):
    return np.array([[cos(theta),sin(theta)],
                     [-sin(theta),cos(theta)]])

def show_plot(map_coords, goal=None, obstacles=None, pause=0, sensors=[]):

    plt.clf()

    # Plot lines representing distance/obstacle detection sensors
    if sensors:
        for sensor in sensors:
            sensor_start = sensor[0]
            sensor_end = sensor[1]
            plt.plot([sensor_start[0], sensor_end[0]], 
                     [sensor_start[1], sensor_end[1]])

    # Plot the walls 
    # Bottom wall from x-min to x_max at y=y_min
    plt.plot([map_coords[0][0], map_coords[0][1]], 
             [map_coords[1][0], map_coords[1][0]], 
             color='red', linewidth=2.0)
    # Top wall from x-min to x_max at y=y_max
    plt.plot([map_coords[0][0], map_coords[0][1]], 
             [map_coords[1][1], map_coords[1][1]], 
             color='red', linewidth=2.0)
    # Left wall from y-min to y_max at x=x_min
    plt.plot([map_coords[0][0], map_coords[0][0]], 
             [map_coords[1][0], map_coords[1][1]], 
             color='red', linewidth=2.0)
    # Right wall from y-min to y_max at x=x_min
    plt.plot([map_coords[0][1], map_coords[0][1]], 
             [map_coords[1][0], map_coords[1][1]], 
             color='red', linewidth=2.0)

    # Plot the obstacles
    fig = plt.gcf()
    ax = fig.gca()

    if obstacles:
        for ii in obstacles:
            obstacle_patch = patches.Rectangle(
                (ii[0][0], ii[0][1]), ii[1][0], ii[1][1],
                facecolor='gray', label='Obstacle')
        
            ax.add_patch(obstacle_patch)
    
    # Plot the goal
    if goal:
        plt.plot(goal[0], goal[1], 'r*', markersize=15, label='Goal')

    # Plot a line showing the position of the robot at each point in the log
    plt.plot(x_log,y_log)
    

    for ii in range(len(th_log)):

        """
        Plot the outline of robot at each point in the log using its heading and position, 
        where the rotation matrix is used to rotate the coordinates that define the 
        outline of the robot to heading, theta. 
        """
        this_shape = rotation_matrix(th_log[ii])@robot_shape

        plt.plot(x_log[ii]+this_shape[0,:],
                 y_log[ii]+this_shape[1,:],
                 'k-')
    
    
    # Get the current heading of the robot
    ii = len(th_log) - 1
    this_shape = rotation_matrix(th_log[ii])@robot_shape

    
    # Plot the outline of robot at the current position in a different colour
    plt.plot(x_log[ii]+this_shape[0,:],
             y_log[ii]+this_shape[1,:],
             'red')
    
    # Set the horizontal and vertical axes to equal length 
    plt.axis('equal')

    """
    Display the figure of the current timestep for the specified number of seconds
    before the code loops and generates a new figure 
    If no pause is specified, show the figure as normal i.e. require that the window
    be closed manually before the code can loop and display the next figure
    """ 
    if pause > 0:
        plt.pause(pause)
    else:
        plt.show()