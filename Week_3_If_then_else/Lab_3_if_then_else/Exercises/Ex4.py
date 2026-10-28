'''
## Exercise 4 - Robot Obstacle Detection

Our robot simulation -- "robot.py" -- now has some code for storing the robot's parameters
and functions for calculating the robot's next state (position and orientation) given its current state. 
Next, let's add some functions for determing whether our robot has collided with an obstacle or left the arena. 
We've added some variables for storing information about the arena the robot is in and an obstacle in the arena.

Add two functions -- "is_inside_arena" which returns True if the robot is inside the arena and "has_collided" which returns True if the robot has hit the obstacle. 
Remember, the robot itself has a radius-- so we need to check for the intersection of two circles to solve this. You can use the code below to test your functions.
'''

# from previous exercises

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

print("Name: ", robot_name)
print("Radius: ", robot_radius_mm)
print("Wheel spacing: ", wheel_separation_mm)
print("x: ", x, "y: ", y, "theta: ", theta)

def average(m, n):
    return 0.5 * (m + n)

def wheel_speed(omega, radius):
    ''' Calculates the linear speed of a robot wheel given angular velocity (omega) and radius'''
    return omega * radius

def robot_speed(omega_left, omega_right, radius):
    ''' Calculates the forward speed of a robot given wheel angular velocities (omega_left, omega_right) and wheel radius'''
    return average(wheel_speed(omega_left, radius), wheel_speed(omega_right, radius))

def turn_rate(left_speed, right_speed, wheel_separation):
    ''' Calculates the turning rate of a two-wheeled differential drive robot given wheel speeds and wheel separation'''
    return (right_speed - left_speed) / wheel_separation

def robot_motion(omega_left, omega_right, wheel_radius, wheel_separation):
    linear_speed_left = wheel_speed(omega_left, wheel_radius)
    linear_speed_right = wheel_speed(omega_right, wheel_radius)
    linear_speed = robot_speed(omega_left, omega_right, wheel_radius)
    angular_speed = turn_rate(linear_speed_left, linear_speed_right, wheel_separation)

    return linear_speed, angular_speed

print(robot_motion(2, 2, wheel_radius_mm, wheel_separation_mm))
print(robot_motion(-2, 2, wheel_radius_mm, wheel_separation_mm))

WORLD_X_MIN = 0.0
WORLD_X_MAX = 1000.0
WORLD_Y_MIN = 0.0
WORLD_Y_MAX = 1000.0

OBSTACLE_CENTRE_X = 500.0
OBSTACLE_CENTRE_Y = 500.0
OBSTACLE_RADIUS = 50

def is_inside_arena(x, y):
    # Your code here
    pass

def has_collided(x, y):
    # Your code here
    pass

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

# --- has_collided ---

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
