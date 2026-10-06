# --- Week 2: Model Answer ---
#
# Goal: Use conditional logic to check a robot's position against
# world boundaries and obstacles.
#

# --- 1. World Definition ---
# World boundaries (in meters).
WORLD_X_MIN = 0.0
WORLD_X_MAX = 100.0
WORLD_Y_MIN = 0.0
WORLD_Y_MAX = 100.0

# A simple rectangular obstacle.
# Defined by its bottom-left corner (x, y) and its dimensions.
OBSTACLE_X = 40.0
OBSTACLE_Y = 30.0
OBSTACLE_WIDTH = 10.0
OBSTACLE_HEIGHT = 40.0

# --- 2. Robot Test Position ---
# For this script, we'll use a fixed, hardcoded robot position for our checks.
robot_x = 15.0
robot_y = 20.0

print(f"--- Checking Robot Position: ({robot_x}, {robot_y}) ---")

# --- 3. Basic Boundary Check ---
is_inside_x_bounds = (robot_x >= WORLD_X_MIN) and (robot_x <= WORLD_X_MAX)
is_inside_y_bounds = (robot_y >= WORLD_Y_MIN) and (robot_y <= WORLD_Y_MAX)

if is_inside_x_bounds and is_inside_y_bounds:
    print("Status: Robot is within world boundaries.")
else:
    print("Status: DANGER! Robot is out of bounds!")

# --- 4. Proximity Warning Check ---
PROXIMITY_MARGIN = 5.0 # Margin for proximity warnings (in meters).

# Test with a new position close to the edge.
robot_x_2 = 98.0
robot_y_2 = 50.0

print(f"\n--- Checking Proximity for Robot at: ({robot_x_2}, {robot_y_2}) ---")

# The order of these checks is important: out-of-bounds is the highest priority.
is_out_of_bounds = not (robot_x_2 >= WORLD_X_MIN and robot_x_2 <= WORLD_X_MAX and \
                       robot_y_2 >= WORLD_Y_MIN and robot_y_2 <= WORLD_Y_MAX)

is_too_close = robot_x_2 < (WORLD_X_MIN + PROXIMITY_MARGIN) or \
               robot_x_2 > (WORLD_X_MAX - PROXIMITY_MARGIN) or \
               robot_y_2 < (WORLD_Y_MIN + PROXIMITY_MARGIN) or \
               robot_y_2 > (WORLD_Y_MAX - PROXIMITY_MARGIN)

if is_out_of_bounds:
    print("Proximity Status: Robot is OUT OF BOUNDS.")
elif is_too_close:
    print("Proximity Status: WARNING! Robot is close to a boundary.")
else:
    print("Proximity Status: Robot is in a safe area.")

# --- 5. Obstacle Collision Check ---
# Use a third test position, this time inside the obstacle.
robot_x_3 = 45.0
robot_y_3 = 50.0

print(f"\n--- Checking Obstacle Collision for Robot at: ({robot_x_3}, {robot_y_3}) ---")

# An obstacle check is only meaningful if the robot is within the world bounds.
if (robot_x_3 >= WORLD_X_MIN and robot_x_3 <= WORLD_X_MAX and \
    robot_y_3 >= WORLD_Y_MIN and robot_y_3 <= WORLD_Y_MAX):

    # Now that we know it's in the world, check for collision with the obstacle.
    is_in_obstacle = (robot_x_3 >= OBSTACLE_X) and \
                     (robot_x_3 <= OBSTACLE_X + OBSTACLE_WIDTH) and \
                     (robot_y_3 >= OBSTACLE_Y) and \
                     (robot_y_3 <= OBSTACLE_Y + OBSTACLE_HEIGHT)

    if is_in_obstacle:
        print("Collision Status: DANGER! Robot has collided with an obstacle!")
    else:
        print("Collision Status: Robot is clear of obstacles.")
else:
    print("Collision Status: Robot is out of bounds, cannot check for obstacles.")
