'''
Using the code from previous weeks, write a new function ```get_new_position``` which returns the final position of the robot. Your function should accept these inputs:
 + total duration of movement in seconds (float)
 + left wheel speed  in rad / s (float)
 + right wheel speed in rad / s(float)
 + step size in seconds (float) - default to 0.1 if not provided
 + initial x (mm), initial y (mm), initial theta (radians) (float x 3) - default to 0 if not provided

 Your function should return the final `x`, `y`, and `theta`.

We have provided some test functions to check your code is correct. 

Next, we can chain together a sequence of moves to follow a set path. For example, we can drive the robot in a square by setting the following wheel velocities:

1. left = 1, right = 1, time = 10 s # Drive straight
2. left = -1, right = 1, time = ??? # Turn 90 degrees anticlockwise
3. left = 1, right = 1, time = 10 s # Drive straight
4. left = -1, right = 1, time = ??? # Turn 90 degrees anticlockwise
5. left = 1, right = 1, time = 10 s # Drive straight
6. left = -1, right = 1, time = ??? # Turn 90 degrees anticlockwise
7. left = 1, right = 1, time = 10 s # Drive straight
8. left = -1, right = 1, time = ??? # Turn 90 degrees anticlockwise

First, work out how long each turn needs to be. (Hint: use your `turn_rate` function to find how fast the robot turns, then think about how long it takes to turn pi/2 radians.)

Each move should start where the previous one finished, so pass the final `x`, `y` and `theta` from one call in as the initial values for the next.

After following that sequence, your robot should be back where it started, facing the same direction. (Note that `theta` will be 2 pi rather than 0 — the same direction, one full turn later.)

Check whether your robot really does return to (0, 0) with the default step size of 0.1 s. If it doesn't, why not? What happens if you use a step size of 0.001 s instead?
'''

import math 

WORLD_X_MIN = 0.0
WORLD_X_MAX = 1000.0
WORLD_Y_MIN = 0.0
WORLD_Y_MAX = 1000.0

OBSTACLE_CENTRE_X = 500.0
OBSTACLE_CENTRE_Y = 500.0
OBSTACLE_RADIUS = 50

"""
--------------------------------------------------------------
Paremeter definition [Week 1]
--------------------------------------------------------------
"""

wheel_separation_in = 5.906   # distance between the two wheels
wheel_radius_in     = 1.378   # radius of each wheel
robot_radius_in     = 3.248   # radius of the robot body

robot_name = "Robby"
robot_radius_mm = robot_radius_in * 25.4
wheel_separation_mm = wheel_separation_in * 25.4
wheel_radius_mm  = wheel_radius_in * 25.4

x = 0
y = 0
theta = 0

"""
--------------------------------------------------------------
Robot motion functions [Week 2]
--------------------------------------------------------------
"""
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
    return average(wheel_speed(omega_left, radius), wheel_speed(omega_right, radius))


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



def is_inside_arena(x, y):
    if x - robot_radius_mm < WORLD_X_MIN:
        return False

    if x + robot_radius_mm > WORLD_X_MAX:
        return False

    if y - robot_radius_mm < WORLD_Y_MIN:
        return False

    if y + robot_radius_mm > WORLD_Y_MAX:
        return False

    return True


def has_collided(x, y):
    if (x-OBSTACLE_CENTRE_X)**2 + (y-OBSTACLE_CENTRE_Y)**2 < (robot_radius_mm + OBSTACLE_RADIUS)**2:
        return True
    return False


#Write your code here
def get_new_position(duration,          # seconds 
                     omega_left,        # rads/second
                     omega_right,       # rads/second
                     dt = 0.1,   # seconds 
                     x_init = 0,        # initial x position
                     y_init = 0,        # initial y position    
                     theta_init = 0     # inital heading angle theta
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

    #Work out how many time steps
    n_steps = int(duration/dt)
    remainder = duration - (n_steps * dt)

    #Calculate robot speeds
    linear_speed, angular_speed = robot_motion( omega_left, 
                                                omega_right, 
                                                wheel_radius_mm, 
                                                wheel_separation_mm)

    #Perform integration steps
    for i in range(0, n_steps):
        x = x + (math.cos(theta) * dt * linear_speed)
        y = y + (math.sin(theta) * dt * linear_speed)
        theta = theta + (dt * angular_speed)

    # If our integration time is not evenly divided by the step size, 
    # we need to perform one final step to catch the remaining time.
    if remainder > 0:
        x = x + remainder * linear_speed * math.cos(theta)
        y = y + remainder * linear_speed * math.sin(theta)
        theta = (theta + remainder * angular_speed)

    return x,y,theta


# Turn on spot speed 

turn_on_spot_speed = turn_rate( wheel_speed(-1, wheel_radius_mm), 
                                wheel_speed(1, wheel_radius_mm),
                                wheel_separation_mm)
print("turn_on_spot_speed", turn_on_spot_speed, "rad/s")

duration_quarter_turn = math.pi/(2*turn_on_spot_speed)
print("duration_quarter_turn", duration_quarter_turn)


# Driving in a square:
x,y,theta = 0,0,0

for i in range(4):
    # 1. Drive straight (left = 1, right = 1, time = 10 s)
    x, y, theta = get_new_position(10, 1, 1, dt = 0.001, 
                                   x_init = x, y_init = y, theta_init = theta)
    print(x,y,theta)

    # 2. Turn 90 degrees anticlockwise (left = -1, right = 1, time = ???)
    x, y, theta = get_new_position(duration_quarter_turn, -1, 1, dt = 0.001, 
                                   x_init = x, y_init = y, theta_init = theta)
    print(x,y,theta)



# # 3. left = 1, right = 1, time = 10 s # Drive straight
# x, y, theta = get_new_position(10, 1, 1)
# print(x,y,theta)

# # 4. left = -1, right = 1, time = ??? # Turn 90 degrees anticlockwise
# x, y, theta = get_new_position(10, -1, 1)
# print(x,y,theta)

# # 5. left = 1, right = 1, time = 10 s # Drive straight
# x, y, theta = get_new_position(10, 1, 1)
# print(x,y,theta)

# # 6. left = -1, right = 1, time = ??? # Turn 90 degrees anticlockwise
# x, y, theta = get_new_position(10, -1, 1)
# print(x,y,theta)

# # 7. left = 1, right = 1, time = 10 s # Drive straight
# x, y, theta = get_new_position(10, 1, 1)
# print(x,y,theta)

# # 8. left = -1, right = 1, time = ??? # Turn 90 degrees anticlockwise
# x, y, theta = get_new_position(10, -1, 1)
# print(x,y,theta)



    

    
    


'''
=================
Test functions below here -- make sure you understand them, but don't edit
=================
'''
def test_is_inside_arena():

    # Robot well inside the arena -- should be inside
    if is_inside_arena(500, 500) == True:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Centre is in-bounds (x=20) but the robot's body pokes through the left wall -- NOT inside
    if is_inside_arena(20, 500) == False:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Centre well beyond the wall -- not inside
    if is_inside_arena(1100, 500) == False:
        print("Test 3 passed")
    else:
        print("Test 3 failed")


def test_has_collided():

    # Robot sitting right on the obstacle -- collision
    if has_collided(500, 500) == True:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Centre is 20 away (outside the obstacle) but the robot's radius still reaches it -- collision
    if has_collided(520, 500) == True:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Far from the obstacle -- no collision
    if has_collided(100, 100) == False:
        print("Test 6 passed")
    else:
        print("Test 6 failed")


def test_get_new_position():

    # Test 1: drive straight forwards for 10 s from the origin.
    # Both wheels at 1 rad/s -> 1 * wheel_radius_mm = 35.0 mm/s, so we expect to move 350.0 mm along x.
    x, y, theta = get_new_position(10, 1, 1)
    expected_x = 10 * wheel_radius_mm
    if abs(x - expected_x) < 1e-5 and abs(y) < 1e-5 and abs(theta) < 1e-5:
        print("Test 1 passed")
    else:
        print("Test 1 failed: got", x, y, theta, "expected", expected_x, 0, 0)

    # Test 2: drive straight backwards for 10 s, starting at (500, 500) facing along +y (theta = pi/2).
    # We should reverse 350.0 mm in the -y direction, and x and theta shouldn't change.
    x, y, theta = get_new_position(10, -1, -1, 0.1, 500, 500, math.pi/2)
    expected_y = 500 - 10 * wheel_radius_mm
    if abs(x - 500) < 1e-5 and abs(y - expected_y) < 1e-5 and abs(theta - math.pi/2) < 1e-5:
        print("Test 2 passed")
    else:
        print("Test 2 failed: got", x, y, theta, "expected", 500, expected_y, math.pi/2)

    # Test 3: turn 180 degrees on the spot (anticlockwise).
    # Turn rate is 2 * wheel_radius_mm / wheel_separation_mm rad/s, so 180 degrees takes pi / turn_rate seconds.
    # Turning on the spot, the position should not change at all.
    t_180 = math.pi * wheel_separation_mm / (2 * wheel_radius_mm)
    x, y, theta = get_new_position(t_180, -1, 1, t_180 / 100)
    if abs(x) < 1e-5 and abs(y) < 1e-5 and abs(theta - math.pi) < 1e-5:
        print("Test 3 passed")
    else:
        print("Test 3 failed: got", x, y, theta, "expected", 0, 0, math.pi)

    # Test 4: arc - left wheel stopped, right wheel at 1 rad/s, for a quarter turn.
    # The robot pivots about its left wheel, so its centre follows a circle of radius wheel_separation_mm / 2,
    # and after a quarter turn it should be at (R, R) facing along +y.
    # Our step-by-step method is only approximate on curves, so we use a small step and a looser tolerance (0.1 mm).
    R = wheel_separation_mm / 2
    t_quarter = math.pi * wheel_separation_mm / (2 * wheel_radius_mm)
    x, y, theta = get_new_position(t_quarter, 0, 1, t_quarter / 1000)
    if abs(x - R) < 0.1 and abs(y - R) < 0.1 and abs(theta - math.pi/2) < 1e-5:
        print("Test 4 passed")
    else:
        print("Test 4 failed: got", x, y, theta, "expected", R, R, math.pi/2)

test_get_new_position()

