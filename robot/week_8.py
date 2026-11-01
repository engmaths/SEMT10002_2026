import math
import random
from robot_plotter_v2 import init_plot, snapshot, show_plot
from math import sin, cos, pi


#I've made these variable names upper case to represent that they are constants (i.e later code shouldn't re-assign them)
WORLD_X_MIN = 0.0
WORLD_X_MAX = 10000.0
WORLD_Y_MIN = 0.0
WORLD_Y_MAX = 10000.0

GOAL_TOLERANCE = 50.0
ANGULAR_GOAL_TOLERANCE = 0.0001

WHEEL_SEPARATION_IN= 5.906   # distance between the two wheels in inches
WHEEL_RADIUS_IN     = 1.378   # radius of each wheel in inches
ROBOT_RADIUS_IN     = 3.248   # radius of the robot body in inches

MAX_WHEEL_SPEED = 10
#Convert to millimetres
WHEEL_SEPARATION_MM = WHEEL_SEPARATION_IN * 25.4
WHEEL_RADIUS_MM = WHEEL_RADIUS_IN * 25.4
ROBOT_RADIUS_MM = ROBOT_RADIUS_IN * 25.4

# ROBOT_FSM = {
#     "GO_TO_GOAL": {"obstacle_detected": "AVOID_1"},
#     "AVOID_1": {"reverse_completed": "AVOID_2"},
#     "AVOID_2": {"turn_completed": "AVOID_3"},
#     "AVOID_3": {"move_forward_completed": "AVOID_4"},
#     "AVOID_4": {"move_forward_completed": "GO_TO_GOAL"}
#     }

ROBOT_FSM = {
    "GO_TO_GOAL": "AVOID_1",
    "AVOID_1": "AVOID_2",
    "AVOID_2": "AVOID_3",
    "AVOID_3": "AVOID_4",
    "AVOID_4": "GO_TO_GOAL"
}


def average(m, n):
    return 0.5 * (m + n)

def wheel_speed(omega, radius):
    ''' 
    Calculates the linear velocity of a wheel given angular velocity 
    (omega) and radius
    '''
    return omega * radius

def robot_speed(omega_left, omega_right, radius):
    ''' 
    Calculates the linear velocity of a robot given wheel angular 
    velocities (omega_left, omega_right) and wheel radius
    '''
    return average(wheel_speed(omega_left, radius), 
                   wheel_speed(omega_right, radius))

def turn_rate(left_speed, right_speed, wheel_separation):
    ''' 
    Calculates the turning rate of a two-wheeled differential drive 
    robot given wheel linear velocity and wheel separation
    '''
    return (right_speed - left_speed) / wheel_separation


def robot_motion(omega_left, omega_right, wheel_radius, wheel_separation):
    ''' 
    Returns the linear velocity and angular velocity of a two-wheeled 
    differential drive robot given wheel linear velocity and wheel separation
    '''
    linear_speed_left = wheel_speed(omega_left, wheel_radius)
    linear_speed_right = wheel_speed(omega_right, wheel_radius)
    linear_speed = robot_speed(omega_left, omega_right, wheel_radius)
    angular_speed = turn_rate(linear_speed_left, linear_speed_right, wheel_separation)

    return linear_speed, angular_speed


# (time, left_speed, right_speed, x=0, y=0, theta=0, dt=0.1)
def get_new_position(duration,          # seconds 
                     omega_left,        # rads/second
                     omega_right,       # rads/second
                     x_init = 0,        # initial x position
                     y_init = 0,        # initial y position    
                     theta_init = 0,    # inital heading angle theta
                     dt = 0.001   # seconds 
                     ):

    """
    Returns the updated coordinates and heading angle of a 
    differential drive robot given the initial cooridnates and heading,
    left and right wheel angular velocities, motion duration, and step 
    size for integrating motion
    """

    x = x_init
    y = y_init
    theta = theta_init

    #Work out how many time steps and the remainder if dt doesn't go into duration exactly
    n_steps = int(duration/dt)
    remainder = duration - (n_steps * dt)

    #Calculate robot speeds
    linear_speed, angular_speed = robot_motion( omega_left, 
                                                omega_right, 
                                                WHEEL_RADIUS_MM, 
                                                WHEEL_SEPARATION_MM)
    #Perform integration steps
    for i in range(0, n_steps):
        x = x + (cos(theta) * dt * linear_speed)
        y = y + (sin(theta) * dt * linear_speed)
        theta = theta + (dt * angular_speed)

    # If our integration time is not evenly divided by the step size, 
    # we need to perform one final step to catch the remaining time.
    if remainder > 0:
        x = x + remainder * linear_speed * cos(theta)
        y = y + remainder * linear_speed * sin(theta)
        theta = (theta + remainder * angular_speed)

    return x,y,theta


def is_inside_arena(x, y):
    #Checks if the robot is inside the arena when placed at position (x, y)
    if x - ROBOT_RADIUS_MM < WORLD_X_MIN:
        return False

    if x + ROBOT_RADIUS_MM > WORLD_X_MAX:
        return False

    if y - ROBOT_RADIUS_MM < WORLD_Y_MIN:
        return False

    if y + ROBOT_RADIUS_MM > WORLD_Y_MAX:
        return False

    return True


def has_collided(x, y, obstacle_x, obstacle_y, obstacle_radius):

    distance_to_obstacle = ((x-obstacle_x)**2 + (y-obstacle_y)**2)**(1/2)

    threshold = ROBOT_RADIUS_MM + obstacle_radius

    #Checks for collisions with an obstacle
    if (x-obstacle_x)**2 + (y-obstacle_y)**2 < (ROBOT_RADIUS_MM + obstacle_radius)**2:
        return True
    return False

def state_transition(robot, current_state):
    """
    Return the state of the robot after transitioning 
    """
    return(robot[current_state])

def run_scenario(controller, start_x, start_y, start_theta, 
                 max_time = 50, goals_x=None, goals_y=None, 
                 obstacle_x=None, obstacle_y=None, 
                 obstacle_radius=None):

    #Set initial parameters
    x = start_x
    y = start_y
    theta = start_theta
    t = 0
    step = 1

    goals = list(zip(goals_x, goals_y))

    #Initialise the plot
    init_plot(x, y, theta)

    # Iterate through a series of points
    for goal_x, goal_y in goals:

        state = 'GO_TO_GOAL'

        # Check to see if we have a goal or not.
        if goal_x and goal_y:
            # If we do, make it into a tuple we can pass to the plotting function
            goal = (goal_x, goal_y)
        else:
            goal = None

        # Check to see if we have an obstacle or not
        if obstacle_x and obstacle_y and obstacle_radius:
            #If we do, make it into a tuple we can pass to the plotting function
            obstacle = (obstacle_x, obstacle_y, obstacle_radius)
        else:
            obstacle = None



        #Show the initial configuration for 0.1 seconds
        show_plot(WORLD_X_MIN, WORLD_X_MAX, WORLD_Y_MIN, WORLD_Y_MAX, goals, obstacle, pause=0.1)

        #Main simulation loop
        while t < max_time:
            #Ask the controller what speeds we should set the robot wheels to.
            left_speed, right_speed = controller(x, y, theta, goal_x, goal_y, 
                                                obstacle_x, obstacle_y, obstacle_radius, state)
            
            #Make sure we don't exceed the maximum allowable speeds.
            left_speed = max(-MAX_WHEEL_SPEED, min(MAX_WHEEL_SPEED, left_speed))
            right_speed = max(-MAX_WHEEL_SPEED, min(MAX_WHEEL_SPEED, right_speed))

            #Integrate for one second
            print(theta)
            x, y, theta = get_new_position(step, left_speed, right_speed, x, y, theta)
            print(theta)

            # # -------------------------------------------------------------
            # # Controller 3
            # # -------------------------------------------------------------
            # if state == 'AVOID_1':
            #     state = 'AVOID_2'

            # elif state == 'AVOID_2' and x <= (obstacle_x-obstacle_radius):
            #     state = 'AVOID_3'

            # elif state == 'AVOID_3':
            #     state = 'AVOID_4'
            
            # elif state == 'AVOID_4' and y >= (obstacle_y+obstacle_radius):
            #     state = 'GO_TO_GOAL'

            # -------------------------------------------------------------
            # Controller 4
            # -------------------------------------------------------------
            
            # if state == 'AVOID_1':
            #     state = 'AVOID_2'

            # elif state == 'AVOID_2':
            #     state = 'AVOID_3'

            # elif state == 'AVOID_3':
            #     state = 'AVOID_4'
            
            # elif state == 'AVOID_4':
            #     state = 'GO_TO_GOAL'

            if state != 'GO_TO_GOAL':
                state = state_transition(ROBOT_FSM, state)
    

            #Draw the updated position
            snapshot(x, y, theta)
            # show_plot(WORLD_X_MIN, WORLD_X_MAX, WORLD_Y_MIN, WORLD_Y_MAX, goal, obstacle, pause=0.1)
            # goals = zip(goals_x, goals_y)
            show_plot(WORLD_X_MIN, WORLD_X_MAX, WORLD_Y_MIN, WORLD_Y_MAX, goals, obstacle, pause=0.1)
            t = t + step

            print(state)

            #Check we're still inside the arena
            if not is_inside_arena(x, y):
                print("Error - robot tried to leave the arena")
                break 

            if obstacle and has_collided(x, y, obstacle_x, obstacle_y, obstacle_radius):
                print("Obstacle_detected")
                # Initiate obstacle avoidance sequence
                if state == 'GO_TO_GOAL':
                    # state = 'AVOID_1'
                    state = state_transition(ROBOT_FSM, state)
                    print(state)

        # #Now the main loop has finished, let's see how close we are to the goal.
        # if goal:
        #     x_error = abs(x - goal_x)
        #     y_error = abs(y - goal_y)
        #     total_error = math.sqrt(x_error**2 + y_error**2)
        #     print("Robot has stopped moving -- distance to goal is:", total_error)
        #     if total_error < GOAL_TOLERANCE:
        #         print ("You reached the goal -- well done!")

            # Let's see how close we are to the goal.
            x_error = abs(x - goal_x)
            y_error = abs(y - goal_y)
            total_error = math.sqrt(x_error**2 + y_error**2)
            print("Robot has stopped moving -- distance to goal is:", total_error)
            if total_error < GOAL_TOLERANCE:
                print ("You reached the goal -- well done!")
                break

        # Plot the map one final time, with a longer (5 seconds) pause so we can inspect 1.
        show_plot(WORLD_X_MIN, WORLD_X_MAX, WORLD_Y_MIN, WORLD_Y_MAX, goals, obstacle, pause=0.1)

def move_linearly_to_goal(error): 
    print('Move to goal')
    # k = 0.0005
    k = 0.001
    speed = k * error
    return speed

def rotate_to_goal(angular_error): 
    print('Rotate to goal')
    k = 2
    speed = k * angular_error
    return speed

def avoid_obstacle(obstacle):
    print('Avoid obstacle')
    while obstacle == True:
        pass

def compute_wheel_speed_for_rotation(angle_degrees):
    """
    Returns the wheel speeds needed to achieve the
    input angle (degrees) in a 1 second turn
    """
    angle_rads = pi * angle_degrees/180

    v_wheel_r = angle_rads * WHEEL_SEPARATION_MM / 2

    omega_r = v_wheel_r / WHEEL_RADIUS_MM
    omega_l = -omega_r

    return omega_l, omega_r

def compute_wheel_speed_for_translation(translation_mm):
    """
    Returns the wheel speeds needed to achieve the
    input translation (mm) in a 1 second move
    """
    omega = translation_mm / WHEEL_RADIUS_MM
    return omega

def generate_lawnmower_sequence(start_x, start_y):

    x, y = start_x, start_y

    goals_x = []
    goals_y = []

    for i in range(2):
        x += 2000
        goals_x.append(x)
        goals_y.append(y)

        y += 8000
        goals_x.append(x)
        goals_y.append(y)

        x+=2000
        goals_x.append(x)
        goals_y.append(y)

        y-= 8000
        goals_x.append(x)
        goals_y.append(y)

    return goals_x, goals_y

def controller_1(x, y, theta, 
                 goal_x, goal_y, 
                 obstacle_x=None, 
                 obstacle_y=None, 
                 obstacle_radius=None, state='GO_TO_GOAL'):

    x_distance = (goal_x - x) #* cos(theta) 
    y_distance = (goal_y - y) #* sin(theta)
    error = (x_distance**2 + y_distance**2)**(1/2)

    if abs(error) > GOAL_TOLERANCE:
        speed = move_linearly_to_goal(error)
    else:
        speed = 0

    return speed, speed 

def controller_2(x, y, theta, goal_x, goal_y, 
                 obstacle_x=None, obstacle_y=None, 
                 obstacle_radius=None, state='GO_TO_GOAL'):

    x_distance = (goal_x - x) #* cos(theta) 
    y_distance = (goal_y - y) #* sin(theta)
    error = (x_distance**2 + y_distance**2)**(1/2)
    goal_angle = math.atan2(y_distance, x_distance)
    angular_error = goal_angle - theta 

    # Turn towards the goal
    if abs(angular_error) > ANGULAR_GOAL_TOLERANCE:
        speed = rotate_to_goal(angular_error)
        return -speed, speed

    # Move towards the goal
    elif abs(error) > GOAL_TOLERANCE:
        speed = move_linearly_to_goal(error)
    
    # Stop
    else:
        speed = 0

    return speed, speed 

def controller_3(x, y, theta, goal_x, goal_y,
                 obstacle_x=None, obstacle_y=None, obstacle_radius=None, state='GO_TO_GOAL'):

    print(state)

    if state == 'GO_TO_GOAL':
        left, right = controller_2(x, y, theta, goal_x, goal_y)

    elif state == 'AVOID_1':
        left, right = compute_wheel_speed_for_rotation(angle_degrees=90)
        print(left, right)

    elif state == 'AVOID_2':
        left, right = MAX_WHEEL_SPEED, MAX_WHEEL_SPEED 

    elif state == 'AVOID_3':
        left, right = compute_wheel_speed_for_rotation(angle_degrees=-90)
        print(left, right)
    
    elif state == 'AVOID_4':
        left, right = MAX_WHEEL_SPEED, MAX_WHEEL_SPEED 

    elif state == 'STOP':
        left, right = 0,0 

    return left, right 

def controller_4(x, y, theta, goal_x, goal_y,
                 obstacle_x=None, obstacle_y=None, obstacle_radius=None, state='GO_TO_GOAL'):

    if state == 'GO_TO_GOAL':
        left, right = controller_2(x, y, theta, goal_x, goal_y)

    elif state == 'AVOID_1':
        left, right = -MAX_WHEEL_SPEED/2, -MAX_WHEEL_SPEED/2

    elif state == 'AVOID_2':
        left, right = compute_wheel_speed_for_rotation(angle_degrees=30)

    elif state == 'AVOID_3':
        left, right = MAX_WHEEL_SPEED/2, MAX_WHEEL_SPEED/2
    
    elif state == 'AVOID_4':
        # left, right = MAX_WHEEL_SPEED, MAX_WHEEL_SPEED 
        left, right = 0,0 

    elif state == 'STOP':
        left, right = 0,0 

    return left, right  


def main():

    #Use this function to determine which scenario to run. 

    # Scenario 1 -- Can you move in a straight line and stop at the goal?
    start_x = 5000
    start_y = 1000
    start_theta = pi / 2
    # goal_x = 5000
    # goal_y = 8000
    goals_x = [5000]
    goals_y = [8000]
    max_time = 100
    # run_scenario(controller_1, start_x, start_y, start_theta, max_time, goal_x, goal_y)
    # run_scenario(controller_1, start_x, start_y, start_theta, max_time, goals_x, goals_y)
    

    # Scenario 2 -- Can you turn and then move in a straight line to the goal?
    start_x = 1000
    start_y = 5000
    start_theta = pi
    goal_x = 1000
    goal_y = 1000
    goals_x = [1000, 2000, 1500]
    goals_y = [1000, 1000, 3000] 
    max_time = 10000
    # run_scenario(controller_2, start_x, start_y, start_theta, max_time, goal_x, goal_y)
    # run_scenario(controller_2, start_x, start_y, start_theta, max_time, goals_x, goals_y)

    # Scenario 2 -- Lawnmower
    start_x = 1000
    start_y = 1000
    start_theta = 0
    goals_x, goals_y = generate_lawnmower_sequence(start_x, start_y) 
    max_time = 10000
    # run_scenario(controller_2, start_x, start_y, start_theta, max_time, goals_x, goals_y)
    
    # Scenario 3 -- Can you naivgate past a fixed obstacle?
    start_x = 5000
    start_y = 1000
    start_theta = pi
    # goal_x = 5000
    # goal_y = 8000
    goals_x = [5000, 9000, 1500]
    goals_y = [9000, 5000, 3000]
    obstacle_x = 5000
    obstacle_y = 5000
    obstacle_radius = 500
    max_time = 10000
    # run_scenario(controller_3, start_x, start_y, start_theta, max_time, goal_x, goal_y, obstacle_x, obstacle_y, obstacle_radius)
    run_scenario(controller_3, start_x, start_y, start_theta, max_time, goals_x, goals_y, obstacle_x, obstacle_y, obstacle_radius)
    
    # Scenario 4 -- Can you navigate past a randomly located obstacle?
    start_x = 100 + 4900 * random.random()
    start_y = 100 + 900 * random.random()
    start_theta = pi
    goal_x = 5000 + (4000 * random.random())
    goal_y = 6000 + (3000 * random.random())
    goals_x = [5000 + (4000 * random.random())]
    goals_y = [6000 + (3000 * random.random())]
    start_x = 1000
    start_y = 1000
    start_theta = 0
    goals_x, goals_y = generate_lawnmower_sequence(start_x, start_y) 
    #Generate an initial obstacle position
    obstacle_x = 2500 + (5000 * random.random())
    obstacle_y = 2500 + (5000 * random.random())
    obstacle_radius = 2000    
    #Regenerate obstacle position until it doesn't overlap the start position or goal position. 
    while (has_collided(start_x, start_y, obstacle_x, obstacle_y, obstacle_radius) or has_collided(goal_x, goal_y, obstacle_x, obstacle_y, obstacle_radius)):
       obstacle_x = 2500 + (5000 * random.random())
       obstacle_y = 2500 + (5000 * random.random())
    
    max_time = 100000
    # run_scenario(controller_4, start_x, start_y, start_theta, max_time, goal_x, goal_y, obstacle_x, obstacle_y, obstacle_radius)
    # run_scenario(controller_4, start_x, start_y, start_theta, max_time, goals_x, goals_y, obstacle_x, obstacle_y, obstacle_radius)
    
if __name__ == "__main__":
    main()
