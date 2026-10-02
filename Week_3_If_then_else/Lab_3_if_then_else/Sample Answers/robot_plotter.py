# simple plotting utility for 2D robot simulator
from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt

robot_size = 50

robot_shape = robot_size*np.array([[-1,0,1,-1],
                                  [-1,1,-1,-1]])

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
    return np.array([[cos(theta),sin(theta)],
                     [-sin(theta),cos(theta)]])

def show_plot():
    plt.plot(x_log,y_log)
    for ii in range(len(th_log)):
        this_shape = rotation_matrix(th_log[ii])@robot_shape
        plt.plot(x_log[ii]+this_shape[0,:],
                 y_log[ii]+this_shape[1,:],'k-')
    plt.axis('equal')
    plt.show()
