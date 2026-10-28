# --- Week 5: Model Answer ---
#
# Goal: Refactor the robot simulation to use data structures, logically
#       grouping world and robot parameters into dictionaries and lists.
#

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- 1. World Definition ---
# A single dictionary to hold all environment parameters. This makes it easy
# to pass environment information to functions.
world = {
    'x_max': 100.0,
    'y_max': 100.0,
    'start_pos': (10.0, 50.0),
    'goal_pos': (80.0, 50.0),
    'goal_tolerance': 1.5,
    'obstacles': [
        {'x': 30.0, 'y': 30.0, 'w': 20.0, 'h': 40.0},
        {'x': 60.0, 'y': 10.0, 'w': 15.0, 'h': 25.0},
    ]
}

# --- 2. Robot Definition ---
# A dictionary representing the robot's complete state.
robot = {
    'x': world['start_pos'][0],
    'y': world['start_pos'][1],
    'heading': 0.0,             # radians
    'state': "MOVING_TO_GOAL",  # The robot's current behaviour
    'wheelbase': 0.5,
    'speed_l': 0.0,
    'speed_r': 0.0
}

# --- 3. Refactored Functions ---
# Functions now accept the main data structures as arguments,
# simplifying their signatures.

def update_robot_state(robot_dict):
    """
    Updates the robot's position and heading based on its current state.
    NOTE: This function modifies the dictionary in-place.
    """
    linear_velocity = (robot_dict['speed_l'] + robot_dict['speed_r']) / 2
    angular_velocity = (robot_dict['speed_r'] - robot_dict['speed_l']) / robot_dict['wheelbase']

    delta_heading = angular_velocity * TIME_STEP
    delta_x = linear_velocity * math.cos(robot_dict['heading']) * TIME_STEP
    delta_y = linear_velocity * math.sin(robot_dict['heading']) * TIME_STEP

    robot_dict['x'] += delta_x
    robot_dict['y'] += delta_y
    robot_dict['heading'] += delta_heading
    return robot_dict

def is_colliding(x, y, world_dict):
    """Checks if a position collides with boundaries or any obstacle in the world."""
    if not (0 <= x <= world_dict['x_max'] and 0 <= y <= world_dict['y_max']):
        return True

    # Iterate through all defined obstacles.
    for obstacle in world_dict['obstacles']:
        if (obstacle['x'] <= x <= obstacle['x'] + obstacle['w'] and \
            obstacle['y'] <= y <= obstacle['y'] + obstacle['h']):
            return True # Collision detected with an obstacle.

    return False

# (Helper functions like calculate_distance and calculate_angle_to_goal remain unchanged)
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_angle_to_goal(robot_x, robot_y, goal_x, goal_y):
    return math.atan2(goal_y - robot_y, goal_x - robot_x)

def plot_robot_path(path, world_dict):
    """Generates a plot of the final simulation path and world layout."""
    x_coords, y_coords = zip(*path)
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.plot(x_coords, y_coords, 'b-', label='Robot Path')
    ax.plot(world_dict['start_pos'][0], world_dict['start_pos'][1], 'go', markersize=10, label='Start')
    ax.plot(world_dict['goal_pos'][0], world_dict['goal_pos'][1], 'r*', markersize=15, label='Goal')

    # Draw all obstacles from the world's obstacle list.
    for obstacle in world_dict['obstacles']:
        ax.add_patch(patches.Rectangle((obstacle['x'], obstacle['y']), obstacle['w'], obstacle['h'], facecolor='gray'))

    ax.set_title("Robot Path Simulation")
    ax.set_xlabel("X Position (m)"), ax.set_ylabel("Y Position (m)")
    ax.set_xlim(0, world_dict['x_max']), ax.set_ylim(0, world_dict['y_max'])
    ax.set_aspect('equal', adjustable='box'), ax.grid(True), ax.legend()
    plt.show()


# --- 4. Main Simulation Loop ---
print("--- Starting Data Structure-driven Simulation ---")

TIME_STEP = 0.1
path_history = [(robot['x'], robot['y'])]
step_count, MAX_STEPS = 0, 2000
wall_follow_steps = 0 # Timer for wall-following duration.

while calculate_distance(robot['x'], robot['y'], world['goal_pos'][0], world['goal_pos'][1]) > world['goal_tolerance']:

    if robot['state'] == "MOVING_TO_GOAL":
        angle_to_goal = calculate_angle_to_goal(robot['x'], robot['y'], world['goal_pos'][0], world['goal_pos'][1])
        if angle_to_goal > robot['heading']: robot['speed_l'], robot['speed_r'] = 1.8, 2.0
        else: robot['speed_l'], robot['speed_r'] = 2.0, 1.8

        # To predict the next move without altering the current state, we work on a copy.
        predicted_robot = update_robot_state(robot.copy())

        if is_colliding(predicted_robot['x'], predicted_robot['y'], world):
            robot['state'] = "FOLLOWING_WALL"
            wall_follow_steps = 150 # Reset the wall-following timer
            robot['speed_l'], robot['speed_r'] = -1.0, 1.0 # Turn away from obstacle

    elif robot['state'] == "FOLLOWING_WALL":
        robot['speed_l'], robot['speed_r'] = 2.0, 1.7
        predicted_robot = update_robot_state(robot.copy())
        if is_colliding(predicted_robot['x'], predicted_robot['y'], world):
            robot['speed_l'], robot['speed_r'] = -1.0, 1.0 # Turn away from corner

        wall_follow_steps -= 1
        if wall_follow_steps <= 0:
            robot['state'] = "MOVING_TO_GOAL"

    # Apply the chosen wheel speeds to update the robot's state and record its path.
    robot = update_robot_state(robot)
    path_history.append((robot['x'], robot['y']))

    step_count += 1
    if step_count >= MAX_STEPS: break

# --- 5. Final Analysis & Visualisation ---
print("\n--- Simulation Finished ---")
plot_robot_path(path_history, world)
