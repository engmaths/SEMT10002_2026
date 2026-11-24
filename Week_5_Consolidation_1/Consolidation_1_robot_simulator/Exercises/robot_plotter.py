# simple plotting utility for 2D robot simulator
from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

robot_size = 3.248 * 25.4
robot_shape = robot_size*np.array([[-1,1,-1,-1],
                                  [-1,0,1,-1]])

x_log = []
y_log = []
th_log = []

def init_plot(x_position,y_position,heading):
    x_log.clear()
    y_log.clear()
    th_log.clear()
    snapshot(x_position,y_position,heading)

def snapshot(x_position,y_position,heading):
    x_log.append(x_position)
    y_log.append(y_position)
    th_log.append(heading)

def rotation_matrix(theta):
    return np.array([[cos(theta),-sin(theta)],
                     [sin(theta),cos(theta)]])

def show_plot(x_min, x_max, y_min, y_max, goal=None, obstacle=None, pause=0):

    plt.clf()
    #plot walls

    plt.plot([x_min, x_max], [y_min, y_min], color='red', linewidth=2.0)
    #This plots the top line of the map- from x-min to x_max at y=y_max
    plt.plot([x_min, x_max], [y_max, y_max], color='red', linewidth=2.0)
    #This plots the left line of the map- from y-min to y_max at x=x_min
    plt.plot([x_min, x_min], [y_min, y_max], color='red', linewidth=2.0)
    #This plots the right line of the map- from y-min to y_max at x=x_min
    plt.plot([x_max, x_max], [y_min, y_max], color='red', linewidth=2.0)

    fig = plt.gcf()
    ax = fig.gca()

    if obstacle:
        obstacle_patch = patches.Circle(
            (obstacle[0], obstacle[1]), obstacle[2],
            facecolor='gray', label='Obstacle')
    
        ax.add_patch(obstacle_patch)
    
    if goal:
        ax.plot(goal[0], goal[1], 'r*', markersize=15, label='Goal')

    #plot robot
    plt.plot(x_log,y_log)
    
    for ii in range(len(th_log)):
        this_shape = rotation_matrix(th_log[ii])@robot_shape
        plt.plot(x_log[ii]+this_shape[0,:],
                 y_log[ii]+this_shape[1,:],'k-')
    
    
    ii = len(th_log) - 1
    this_shape = rotation_matrix(th_log[ii])@robot_shape

    plt.plot(x_log[ii]+this_shape[0,:],
                y_log[ii]+this_shape[1,:],'red')
    plt.axis('equal')

    if pause > 0:
        plt.pause(pause)
    else:
        plt.show()