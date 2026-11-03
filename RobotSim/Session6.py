# --- Week 6: Model Answer ---
#
# Goal: To read the world configuration from a custom TXT file and to save
#       the simulation results to files and plots.
#

import math
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- 1. File Parsing ---

def load_world_from_txt(filepath):
    """
    Parses a custom .txt map file to build the world configuration.

    The expected format uses keywords (case-insensitive):
      - size [width] [height]
      - start [x] [y]
      - goal [x] [y]
      - obstacle [x] [y] [width] [height]
    Lines starting with '#' or empty lines are ignored.

    Args:
        filepath (str): The path to the map file.

    Returns:
        dict: A world dictionary containing the parsed data.
    """
    world_data = {'obstacles': []}
    with open(filepath, 'r') as f:
        for line in f:
            # Ignore empty lines and comments
            clean_line = line.strip()
            if not clean_line or clean_line.startswith('#'):
                continue

            # Parse line content
            parts = clean_line.split()
            keyword = parts[0].lower()
            values = [float(v) for v in parts[1:]]

            if keyword == 'size' and len(values) == 2:
                world_data['x_max'], world_data['y_max'] = values
            elif keyword == 'start' and len(values) == 2:
                world_data['start_pos'] = tuple(values)
            elif keyword == 'goal' and len(values) == 2:
                world_data['goal_pos'] = tuple(values)
            elif keyword == 'obstacle' and len(values) == 4:
                obs_dict = {'x': values[0], 'y': values[1], 'w': values[2], 'h': values[3]}
                world_data['obstacles'].append(obs_dict)

    # Add default parameters not specified in the file
    world_data['goal_tolerance'] = 1.5
    return world_data

# --- 2. Core Simulation Functions ---

def update_robot_state(robot_dict):
    """Updates the robot's state in-place for one time step."""
    linear_velocity = (robot_dict['speed_l'] + robot_dict['speed_r']) / 2
    angular_velocity = (robot_dict['speed_r'] - robot_dict['speed_l']) / robot_dict['wheelbase']
    delta_heading = angular_velocity * TIME_STEP
    delta_x = linear_velocity * math.cos(robot_dict['heading']) * TIME_STEP
    delta_y = linear_velocity * math.sin(robot_dict['heading']) * TIME_STEP
    robot_dict['x'] += delta_x; robot_dict['y'] += delta_y; robot_dict['heading'] += delta_heading
    return robot_dict

def is_colliding(x, y, world_dict):
    """Checks for collision with world boundaries or any obstacle."""
    if not (0 <= x <= world_dict['x_max'] and 0 <= y <= world_dict['y_max']): return True
    for obstacle in world_dict['obstacles']:
        if (obstacle['x'] <= x <= obstacle['x'] + obstacle['w'] and \
            obstacle['y'] <= y <= obstacle['y'] + obstacle['h']): return True
    return False

def calculate_distance(x1, y1, x2, y2):
    """Calculates Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_angle_to_goal(robot_x, robot_y, goal_x, goal_y):
    """Calculates the global angle from the robot to the goal."""
    return math.atan2(goal_y - robot_y, goal_x - robot_x)

# --- 3. Plotting and Visualisation ---

def plot_robot_path(path, world_dict):
    """Generates a plot of the final simulation path and world layout."""
    x_coords, y_coords = zip(*path)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x_coords, y_coords, 'b-', label='Robot Path')
    ax.plot(world_dict['start_pos'][0], world_dict['start_pos'][1], 'go', markersize=10, label='Start')
    ax.plot(world_dict['goal_pos'][0], world_dict['goal_pos'][1], 'r*', markersize=15, label='Goal')
    for obstacle in world_dict['obstacles']:
        ax.add_patch(patches.Rectangle((obstacle['x'], obstacle['y']), obstacle['w'], obstacle['h'], facecolor='gray'))
    ax.set_title("Robot Path Simulation"), ax.set_xlabel("X Position (m)"), ax.set_ylabel("Y Position (m)")
    ax.set_xlim(0, world_dict['x_max']), ax.set_ylim(0, world_dict['y_max'])
    ax.set_aspect('equal', adjustable='box'), ax.grid(True), ax.legend()
    plt.show()

def plot_distance_analytics(distance_history):
    """Plots the robot's distance to the goal at each step of the simulation."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(distance_history)
    ax.set_title("Distance to Goal Over Time"), ax.set_xlabel("Simulation Step"), ax.set_ylabel("Distance (m)")
    ax.grid(True)
    plt.show()

# --- 4. Main Execution ---

# --- Load and Initialize ---
try:
    world = load_world_from_txt('map.txt')
    print("Successfully loaded map.txt.")
except FileNotFoundError:
    print("Error: map.txt not found! Please create the map file.")
    exit() # Stop execution if the map can't be loaded

robot = {'x': world['start_pos'][0], 'y': world['start_pos'][1], 'heading': 0.0, 'state': "MOVING_TO_GOAL", 'wheelbase': 0.5, 'speed_l': 0.0, 'speed_r': 0.0}
TIME_STEP = 0.1
step_count, MAX_STEPS = 0, 2000
wall_follow_steps_remaining = 0

# History lists for storing simulation data
path_history = [(robot['x'], robot['y'])]
distance_to_goal_history = [calculate_distance(robot['x'], robot['y'], world['goal_pos'][0], world['goal_pos'][1])]

# --- Run Simulation Loop ---
print("Starting simulation...")
while calculate_distance(robot['x'], robot['y'], world['goal_pos'][0], world['goal_pos'][1]) > world['goal_tolerance']:
    if robot['state'] == "MOVING_TO_GOAL":
        angle_to_goal = calculate_angle_to_goal(robot['x'], robot['y'], world['goal_pos'][0], world['goal_pos'][1])
        if angle_to_goal > robot['heading']: robot['speed_l'], robot['speed_r'] = 1.8, 2.0
        else: robot['speed_l'], robot['speed_r'] = 2.0, 1.8

        # Predict next move on a copy of the robot to check for collisions
        predicted_robot = update_robot_state(robot.copy())
        if is_colliding(predicted_robot['x'], predicted_robot['y'], world):
            robot['state'] = "FOLLOWING_WALL"
            wall_follow_steps_remaining = 150
            robot['speed_l'], robot['speed_r'] = -1.0, 1.0 # Turn sharply

    elif robot['state'] == "FOLLOWING_WALL":
        robot['speed_l'], robot['speed_r'] = 2.0, 1.7 # Hug the wall
        predicted_robot = update_robot_state(robot.copy())
        if is_colliding(predicted_robot['x'], predicted_robot['y'], world):
            robot['speed_l'], robot['speed_r'] = -1.0, 1.0 # Turn at corner

        wall_follow_steps_remaining -= 1
        if wall_follow_steps_remaining <= 0:
            robot['state'] = "MOVING_TO_GOAL"

    # Update state and record data for this step
    robot = update_robot_state(robot)
    path_history.append((robot['x'], robot['y']))
    distance_to_goal_history.append(calculate_distance(robot['x'], robot['y'], world['goal_pos'][0], world['goal_pos'][1]))

    step_count += 1
    if step_count >= MAX_STEPS:
        print("Max steps reached.")
        break
print("Simulation finished.")

# --- Save Results ---
output_filename = 'path_history.csv'
try:
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Step', 'X_Position', 'Y_Position'])
        for i, pos in enumerate(path_history):
            writer.writerow([i, pos[0], pos[1]])
    print(f"Path history saved to {output_filename}.")
except IOError:
    print(f"Error: Could not write to file {output_filename}.")

# --- Generate Plots ---
print("Generating plots...")
plot_robot_path(path_history, world)
plot_distance_analytics(distance_to_goal_history)
