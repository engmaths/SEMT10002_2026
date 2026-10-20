import math
import random
from robot_plotter import init_plot, snapshot, show_plot


#I've made these variable names upper case to represent that they are constants (i.e later code shouldn't re-assign them)
WORLD_X_MIN = 0.0
WORLD_X_MAX = 10000.0
WORLD_Y_MIN = 0.0
WORLD_Y_MAX = 10000.0

GOAL_TOLERANCE = 50.0

WHEEL_SEPARATION_IN= 5.906   # distance between the two wheels in inches
WHEEL_RADIUS_IN     = 1.378   # radius of each wheel in inches
ROBOT_RADIUS_IN     = 3.248   # radius of the robot body in inches

MAX_WHEEL_SPEED = 10
#Convert to millimetres
WHEEL_SEPARATION_MM = WHEEL_SEPARATION_IN * 25.4
WHEEL_RADIUS_MM = WHEEL_RADIUS_IN * 25.4
ROBOT_RADIUS_MM = ROBOT_RADIUS_IN * 25.4

def average(m, n):
    return 0.5 * (m + n)

def wheel_speed(omega, radius):
    ''' Calculates the linear speed of a robot wheel given angular velocity (omega) and radius'''
    return omega * radius


def robot_speed(omega_left, omega_right, radius):
    ''' Calculates the forward speed of a robot given wheel angular velocities (omega_left, omega_right) and wheel radius'''
    return average(wheel_speed(omega_left, radius), wheel_speed(omega_right, radius))


def turn_rate(left_speed, right_speed, wheel_separation):
    ''' Calculates the turning rate of a two-wheeled differential drive robot given  linear wheel speeds and wheel separation'''
    return (right_speed - left_speed) / wheel_separation


def robot_motion(omega_left, omega_right, wheel_radius, wheel_separation):
    ''' calculates the linear and angular speed of a two-wheeled differential drive robot given angular wheel speeds and wheel radius and separation'''
    linear_speed_left = wheel_speed(omega_left, wheel_radius)
    linear_speed_right = wheel_speed(omega_right, wheel_radius)
    linear_speed = robot_speed(omega_left, omega_right, wheel_radius)
    angular_speed = turn_rate(linear_speed_left, linear_speed_right, wheel_separation)

    return linear_speed, angular_speed


def get_new_position(time, left_speed, right_speed, x=0, y=0, theta=0, dt=0.1):
    '''
    Integrates robot position given angular wheel speeds
    '''

    #Work out how many time steps
    n_steps = int(time / dt) 
    #Check for remaining time
    remainder = time - (n_steps * dt)

    #Calculate robot speeds
    linear_speed, angular_speed = robot_motion(left_speed, right_speed, WHEEL_RADIUS_MM, WHEEL_SEPARATION_MM)

    #Perform integration steps
    for step in range(n_steps):
        x = x + dt * linear_speed * math.cos(theta)
        y = y + dt * linear_speed * math.sin(theta)
        theta = (theta + dt * angular_speed)

    #If our integration time is not evenly divided by the step size, we need to perform one final step to catch the remaining time.
    if remainder > 0:
        x = x + remainder * linear_speed * math.cos(theta)
        y = y + remainder * linear_speed * math.sin(theta)
        theta = (theta + remainder * angular_speed)

    return x, y, theta


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
    #Checks for collisions with an obstacle

    if (x-obstacle_x)**2 + (y-obstacle_y)**2 < (ROBOT_RADIUS_MM + obstacle_radius)**2:
        return True
    return False


def run_scenario(controller, start_x, start_y, start_theta, max_time = 50, goal_x=None, goal_y=None, obstacle_x=None, obstacle_y=None, obstacle_radius=None):

    #Set initial parameters
    x = start_x
    y = start_y
    theta = start_theta
    t = 0
    step = 1

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

    #Initialise the plot
    init_plot(x, y, theta)
    #Show the initial configuration for 0.1 seconds
    show_plot(WORLD_X_MIN, WORLD_X_MAX, WORLD_Y_MIN, WORLD_Y_MAX, goal, obstacle, pause=0.1)

    #Main simulation loop
    while t < max_time:
        #Ask the controller what speeds we should set the robot wheels to.
        left_speed, right_speed = controller(x, y, theta, goal_x, goal_y, obstacle_x, obstacle_y, obstacle_radius)
        #Make sure we don't exceed the maximum allowable speeds.
        left_speed = max(-MAX_WHEEL_SPEED, min(MAX_WHEEL_SPEED, left_speed))
        right_speed = max(-MAX_WHEEL_SPEED, min(MAX_WHEEL_SPEED, right_speed))
        #Integrate for one second
        x, y, theta = get_new_position(step, left_speed, right_speed, x, y, theta)
        #Draw the updated position
        snapshot(x, y, theta)
        show_plot(WORLD_X_MIN, WORLD_X_MAX, WORLD_Y_MIN, WORLD_Y_MAX, goal, obstacle, pause=0.1)
        t = t + step

        #Check we're still inside the arena
        if not is_inside_arena(x, y):
            print("Error - robot tried to leave the arena")
            break 
        #Check we haven't collided with the obstacle
        if obstacle and has_collided(x, y, obstacle_x, obstacle_y, obstacle_radius):
            print("Error - robot collised with the obstacle")
            break

    #Now the main loop has finished, let's see how close we are to the goal.
    if goal:
        x_error = abs(x - goal_x)
        y_error = abs(y - goal_y)
        total_error = math.sqrt(x_error**2 + y_error**2)
        print("Robot has stopped moving -- distance to goal is:", total_error)
        if total_error < GOAL_TOLERANCE:
            print ("You reached the goal -- well done!")

    # Plot the map one final time, with a longer (5 seconds) pause so we can inspect 1.
    show_plot(WORLD_X_MIN, WORLD_X_MAX, WORLD_Y_MIN, WORLD_Y_MAX, goal, obstacle, pause=5.0)

def controller_1(x, y, theta, goal_x, goal_y, obstacle_x=None, obstacle_y=None, obstacle_radius=None):

    left = random.random()
    right = random.random()

    return left, right 

def controller_2(x, y, theta, goal_x, goal_y, obstacle_x=None, obstacle_y=None, obstacle_radius=None):

    left = random.random()
    right = random.random()

    return left, right 

def controller_3(x, y, theta, goal_x, goal_y, obstacle_x=None, obstacle_y=None, obstacle_radius=None):

    left = random.random()
    right = random.random()

    return left, right 

def controller_4(x, y, theta, goal_x, goal_y, obstacle_x=None, obstacle_y=None, obstacle_radius=None):
    '''
    For controller 4, you should *not* use obstacle_x, obstacle_y or obstacle_radius directly. 
    You can pass them as inputs to has_collided (and use the the return value it outputs).
    But no direct acess from within this function!
    ''' 

    left = random.random()
    right = random.random()

    return left, right 


def main():

    #Use this function to determine which scenario to run. 

    # Scenario 1 -- Can you move in a straight line and stop at the goal?
    start_x = 5000
    start_y = 1000
    start_theta = math.pi / 2
    goal_x = 5000
    goal_y = 8000
    max_time = 100
    run_scenario(controller_1, start_x, start_y, start_theta, max_time, goal_x, goal_y)

    # Scenario 2 -- Can you turn and then move in a straight line to the goal?
    '''
    start_x = 5000
    start_y = 1000
    start_theta = math.pi
    goal_x = 5000
    goal_y = 8000
    max_time = 100
    run_scenario(controller_2, start_x, start_y, start_theta, max_time, goal_x, goal_y)
    '''

    # Scenario 3 -- Can you naivgate past a fixed obstacle?
    '''
    start_x = 5000
    start_y = 1000
    start_theta = math.pi
    goal_x = 5000
    goal_y = 8000
    obstacle_x = 5000
    obstacle_y = 5000
    obstacle_radius = 500
    max_time = 100
    run_scenario(controller_3, start_x, start_y, start_theta, max_time, goal_x, goal_y, obstacle_x, obstacle_y, obstacle_radius)
    '''

    # Scenario 4 -- Can you navigate past a randomly located obstacle?
    '''
    start_x = 100 + 4900 * random.random()
    start_y = 100 + 900 * random.random()
    start_theta = math.pi
    goal_x = 5000 + (4000 * random.random())
    goal_y = 6000 + (3000 * random.random())
    #Generate an initial obstacle position
    obstacle_x = 2500 + (5000 * random.random())
    obstacle_y = 2500 + (5000 * random.random())
    obstacle_radius = 2000    
    #Regenerate obstacle position until it doesn't overlap the start position or goal position. 
    while (has_collided(start_x, start_y, obstacle_x, obstacle_y, obstacle_radius) or has_collided(goal_x, goal_y, obstacle_x, obstacle_y, obstacle_radius)):
       obstacle_x = 2500 + (5000 * random.random())
       obstacle_y = 2500 + (5000 * random.random())
    
    max_time = 200
    run_scenario(controller_4, start_x, start_y, start_theta, max_time, goal_x, goal_y, obstacle_x, obstacle_y, obstacle_radius)
    '''

if __name__ == "__main__":
    main()
