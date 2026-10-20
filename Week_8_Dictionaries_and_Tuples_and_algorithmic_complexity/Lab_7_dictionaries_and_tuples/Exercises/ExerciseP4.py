'''
## Task

This file contains a sample answer for Portfolio Exercsies P1-3

Modify the `detect_obstacles` function so that an obstacle is only detected 
if it intersects the line representing the detection range of one or more 
of the three sensors.

Your modified function header should have the following form. Notice that compared to the example solution in *ExerciseP4.py*:
- there are two new input arguments `sensor_angles`, `sensor_range`
- the function outputs are unchanged, it returns `obstacle_detected`, `obstacle_type`


def detect_obstacles(   robot_x_position, 
                        robot_y_position, 
                        sensor_angles,
                        sensor_range,
                        obstacles,
                        map_x_min=map_x_min,
                        map_x_max=map_x_max,
                        map_y_min=map_y_min,
                        map_y_max=map_y_max):
    
    """
    Determines whether the robot has collided with a wall or obstacle by checking 
    for intersections between the sensor’s detection line and the line segments 
    that represent walls or obstacles.

    Parameters
    ----------
    robot_x_position (int or float): x coordinate of robot
    robot_y_position (int or float): y coordinate of robot
    sensor_angles(list of ints or floats): The angles of the sensors found using the current robot heading 
                                           [robot_heading-pi/4, robot_heading, robot_heading+pi/4] 
    sensor_range(int or float): The range within which obstacles can be detected by each sensor i.e. the length of the 
                                line representing the sensor (300mm) 
    obstacles (list of tuples): List of obstacle positions and dimensions.
                                Each obstacle is represented as ((position_x, position_y)
    map_x_min (int or float) : Minimum x coordinate of rectangular boundary
    map_x_max (int or float) : Maximum x coordinate of rectangular boundary
    map_y_min (int or float) : Minimum y coordinate of rectangular boundary
    map_y_max (int or float) : Maximum y coordinate of rectangular boundary

    Returns
    -------
    obstacle_detected (Boolean): True if obstacle detected, else False
    obstacle_type (str): The type of obstacle detected 'obstacle' or 'wall'
    """

'''

from robot_plotter import init_plot, snapshot, show_plot
from math import sin, cos, atan2, sqrt, pi
from random import random
from time import perf_counter
import csv

# Navigation mode: 'random_walk_mode' or 'goal_seek_mode'
mode = 'random_walk_mode' # 'goal_seek_mode' 

# Obstacle avoidance
avoid_obstacles = True

# Simulation start time
start_time = perf_counter() 

# Robot log file name
log_file_name = 'log_file.csv'

# Constants about the robot
robot_name = "Daneel"
robot_radius = 160
wheel_separation = 150
wheel_radius = 35

# Map information
map_x_min = 0
map_x_max = 5000
map_y_min  = 0
map_y_max = 5000
map_coords = ((map_x_min, map_x_max), 
              (map_y_min, map_y_max))

# Obstacles described using the format ((position_x, position_y), (width, height))
obstacles = [((100, 2250), (4000, 500)),
             ((3000, 3000), (800, 1500)),
             ((1500, 500), (600, 600))
            ]

# Goal position
goal = (1000, 4000)

# The number of timesteps to simulate 
num_steps = 50

# The timestep in seconds
delta_t = 1 

def compute_new_position(robot_x_position, robot_y_position, robot_heading, 
                            linear_speed_left, linear_speed_right, 
                            wheel_separation, delta_t):
    """
    Computes the new x,y position and heading (theta) of the robot

    Parameters
    ----------
    robot_x_position (int or float): previous x coordinate of robot
    robot_y_position (int or float): previous y coordinate of robot
    robot_heading (int or float): previous heading
    linear_speed_left (int or float): left wheel linear speed 
    linear_speed_right (int or float): right wheel linear speed
    wheel_separation (int or float): distance between left and right wheel
    delta_t (int or float): period that the robot moves for in seconds

    Returns
    -------
    x, y, theta (ints or floats): The new position and heading
    """

    # Compute angular speed of the robot
    ang_speed_robot = (linear_speed_left - linear_speed_right) / wheel_separation

    # Multiply angular speed by time to get angular displacement
    angle_change = ang_speed_robot * delta_t

    # Compute average of left and right wheel speed
    ave_speed = 0.5 * (linear_speed_left + linear_speed_right)

    # Compute sinc
    if angle_change**2 < 0.1**2:
        # Taylor series for small values
        the_sinc = 1 - (0.25 * angle_change**2 / 6.0)

    else:
        the_sinc = sin(0.5 * angle_change) / (0.5 * angle_change)

    # Update position
    robot_x_position = robot_x_position + ave_speed * delta_t * the_sinc * sin(robot_heading + 0.5 * angle_change)
    robot_y_position = robot_y_position + ave_speed * delta_t * the_sinc * cos(robot_heading + 0.5 * angle_change)

    # Update heading
    robot_heading = robot_heading + angle_change

    return robot_x_position, robot_y_position, robot_heading

def random_walk():

    """
    Returns randomly generated linear wheel speed for left and right wheel
    """

    # Set the angular wheel speeds to be random numbers between 0 and 5
    ang_speed_left = 5 * random()
    ang_speed_right = 5 * random()

    # Convert angular speeds into linear speeds
    linear_speed_left = ang_speed_left * wheel_radius
    linear_speed_right = ang_speed_right * wheel_radius
    
    return linear_speed_left, linear_speed_right

def goal_seek(step, angle_change, distance_robot, 
              delta_t, wheel_separation, num_steps):
    
    """
    Moves robot to goal position in a straight line over 
    specified number of timesteps

    Parameters
    ----------
    step (int): Current step in simulation
    angle_change (int or float): Angle to move through to point robot heading towards goal
    distance_robot (int or float): Distance from robot original position to goal
    delta_t (int or float): Period that the robot moves for in seconds
    wheel_separation (int or float): Distance between left and right wheel
    num_steps (int): Total number of steps in simulation
    delta_t (int or float): Period that the robot moves for in seconds

    Returns
    -------
    linear_speed_left, linear_speed_right (ints or floats): The left and right wheel 
    speed for the current step in the simulation
    """
    # Turn to face heading
    if step == 0:

        # Compute wheel displacement from robot angular displacement
        linear_displacement_left =  angle_change * wheel_separation / 2
        linear_displacement_right = -linear_displacement_left

        # Compute wheel linear speed
        linear_speed_left = linear_displacement_left / delta_t
        linear_speed_right = linear_displacement_right / delta_t

    # Move in straight line to heading
    else:

        # Compute linear speed of robot
        ave_speed = distance_robot / (num_steps - 1)

        # Compute wheel linear speeds
        linear_speed_left = linear_speed_right = ave_speed

    return linear_speed_left, linear_speed_right

def detect_obstacles(   robot_x_position, 
                        robot_y_position, 
                        obstacles,
                        map_x_min=map_x_min,
                        map_x_max=map_x_max,
                        map_y_min=map_y_min,
                        map_y_max=map_y_max):
    
    """
    Detects if the robot has collided with a wall or obstacle

    Parameters
    ----------
    robot_x_position (int or float): x coordinate of robot
    robot_y_position (int or float): y coordinate of robot
    obstacles (list of tuples): List of obstacle positions and dimensions.
                                Each obstacle is represented as ((position_x, position_y)
    map_x_min (int or float) : Minimum x coordinate of rectangular boundary
    map_x_max (int or float) : Maximum x coordinate of rectangular boundary
    map_y_min (int or float) : Minimum y coordinate of rectangular boundary
    map_y_max (int or float) : Maximum y coordinate of rectangular boundary

    Returns
    -------
    obstacle_detected (Boolean): True if obstacle detected, else False
    obstacle_type (str): 'obstacle' or 'wall'
    """

    # Initailise variables
    obstacle_detected = False
    obstacle_type = None

    # Detect obstacles    
    for ii in obstacles:
        obstacle_x = ii[0][0]
        obstacle_y = ii[0][1]
        obstacle_width = ii[1][0]
        obstacle_height = ii[1][1]

        if (obstacle_x < robot_x_position < obstacle_x + obstacle_width and 
            obstacle_y < robot_y_position < obstacle_y + obstacle_height):

            obstacle_detected = True
            obstacle_type = 'obstacle'

    # Detect edges of map
    if (robot_x_position > map_x_max or
        robot_x_position < map_x_min or
        robot_y_position > map_y_max or
        robot_y_position < map_y_min):

        obstacle_detected = True
        obstacle_type = 'wall'

    return obstacle_detected, obstacle_type

def avoid_obstacle_maneuver(wheel_separation):
        
    """
    Returns wheel speed for left and right wheel to turn 180 degrees 
    on the spot in one timestep (1 second)
    """
    linear_displacement_left =  pi * wheel_separation / 2
    linear_displacement_right = -linear_displacement_left

    linear_speed_left = linear_displacement_left / delta_t
    linear_speed_right = linear_displacement_right / delta_t 

    return linear_speed_left, linear_speed_right

def update_log_file(robot_x_position, 
                    robot_y_position,
                    robot_heading, 
                    obstacle_type):

    """
    Appends a new entry to the robot's log file, recording the timestamp,
    position, heading, and any detected obstacle or wall collision.

    Parameters
    ----------
    robot_x_position (int or float) : x coordinate of robot
    robot_y_position (int or float) : y coordinate of robot
    robot heading (int or float) : The robot's heading in radians 
    obstacles (list of tuples): List of obstacle positions and dimensions.
                                Each obstacle is represented as ((position_x, position_y)
    """

    # Generate time stamp
    time_now = perf_counter()
    time_stamp = round((time_now - start_time), 3)

    # Generate state information
    if obstacle_type==None:
        state = ''
    else:
        state = 'Collision with ' + obstacle_type

    # Generate position information
    robot_position = [robot_x_position, robot_y_position] 
    for ii in range(len(robot_position)):
        robot_position[ii] = round(robot_position[ii], 3)

    # Generate heading information 
    robot_heading = round(robot_heading, 3)

    # Generate row to write to log file
    row = [time_stamp, robot_position, robot_heading, state]
    
    # Open the CSV file in append mode
    with open(log_file_name, 'a', newline='') as file:
        writer = csv.writer(file)

        # Append a single row
        writer.writerow(row)  


def main():
    """
    Runs the robot navigation simulation.

    This function initializes the robot state, sets up the plot and log file,
    and then simulates the robot's motion for a fixed number of timesteps.
    Depending on the configured mode ('random_walk_mode' or 'goal_seek_mode'),
    the robot either moves randomly or advances toward a predefined goal.

    The simulation includes:
    - Position and heading updates using differential-drive kinematics.
    - Optional obstacle and wall detection with automatic avoidance maneuvers.
    - Visualisation of the robot's trajectory and the map environment.
    - Logging of timestamps, positions, headings, and collision events
      to a CSV log file.
      """

    # Initial robot configuration
    robot_x_position = 500
    robot_y_position = 500
    robot_heading = 0

    # Initialise visualisation
    init_plot(robot_x_position, 
              robot_y_position, 
              robot_heading)
    
    # Initialise log file with column headings
    with open(log_file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Time (s)','Position [x,y]',
                         'Orientation (rads)','State information']) 

    # Compute angle to turn robot to face goal
    angle_change = atan2(goal[0] - robot_x_position, 
                         goal[1] - robot_y_position) - robot_heading
    
    print('Angle to turn is', angle_change, 'radians')

    # Compute distance to goal 
    distance_robot = sqrt((goal[0] - robot_x_position)**2 + 
                          (goal[1] - robot_y_position)**2)
    
    print('Distance to travel is', distance_robot)

    for step in range(num_steps):

        if mode == 'goal_seek_mode':
            linear_speed_left, linear_speed_right = goal_seek(step, 
                                                              angle_change, 
                                                              distance_robot,
                                                              delta_t, 
                                                              wheel_separation, 
                                                              num_steps)
            
        elif mode == 'random_walk_mode':
            linear_speed_left, linear_speed_right = random_walk()

        # Compute new position and orientation
        robot_x_position_new, robot_y_position_new, robot_heading_new = compute_new_position(robot_x_position, 
                                                                                                robot_y_position, 
                                                                                                robot_heading, 
                                                                                                linear_speed_left, 
                                                                                                linear_speed_right, 
                                                                                                wheel_separation, 
                                                                                                delta_t)                   

        # OBSTACLE AVOIDANCE 
        if avoid_obstacles:
            obstacle_detected, obstacle_type = detect_obstacles(robot_x_position_new, 
                                                                robot_y_position_new, 
                                                                obstacles)

            if obstacle_detected:

                # Turn 180 degrees on the spot if collision with obstacle is detected 
                linear_speed_left, linear_speed_right = avoid_obstacle_maneuver(wheel_separation)

                # Compute new position and orientation
                robot_x_position_new, robot_y_position_new, robot_heading_new = compute_new_position(robot_x_position, 
                                                                                                        robot_y_position, 
                                                                                                        robot_heading, 
                                                                                                        linear_speed_left, 
                                                                                                        linear_speed_right, 
                                                                                                        wheel_separation, 
                                                                                                        delta_t)
        else:
            obstacle_type = None

        # Update robot state
        robot_x_position = robot_x_position_new
        robot_y_position = robot_y_position_new
        robot_heading = robot_heading_new

        # Plot robot at current state
        snapshot(robot_x_position, robot_y_position, robot_heading)
        
        # Update log file
        update_log_file(robot_x_position, 
                         robot_y_position, 
                         robot_heading, 
                         obstacle_type)

        # Display current frame 
        show_plot(map_coords, goal=goal, obstacles=obstacles, pause=0.1)

    # Display final frame 
    show_plot(map_coords, goal=goal, obstacles=obstacles)

if __name__ == '__main__':
    main()