# --- Consolidation Exercise: Model Answer (with Plotting) ---
#
# Goal: Implement and visualize a "Bug Algorithm" navigator using a state
#       machine, with matplotlib used for plotting the final path.
#

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- 1. Simulation Setup ---
WORLD_X_MAX = 100.0
WORLD_Y_MAX = 100.0
WHEELBASE = 0.5
TIME_STEP = 0.1
OBSTACLE = {'x': 30.0, 'y': 30.0, 'w': 20.0, 'h': 40.0}
START_POS = (10.0, 50.0)
GOAL_POS = (80.0, 50.0)
GOAL_TOLERANCE = 1.5

# --- 2. Helper Functions ---

def update_robot_state(x, y, heading, speed_l, speed_r):
    """Calculates the new state of the robot for one time step."""
    linear_velocity = (speed_l + speed_r) / 2
    angular_velocity = (speed_r - speed_l) / WHEELBASE
    delta_heading = angular_velocity * TIME_STEP
    delta_x = linear_velocity * math.cos(heading) * TIME_STEP
    delta_y = linear_velocity * math.sin(heading) * TIME_STEP
    return x + delta_x, y + delta_y, heading + delta_heading

def is_colliding(x, y, obstacle):
    """Checks if a position collides with boundaries or the obstacle."""
    if not (0 <= x <= WORLD_X_MAX and 0 <= y <= WORLD_Y_MAX): return True
    if (obstacle['x'] <= x <= obstacle['x'] + obstacle['w'] and \
        obstacle['y'] <= y <= obstacle['y'] + obstacle['h']): return True
    return False

def calculate_distance(x1, y1, x2, y2):
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_angle_to_goal(robot_x, robot_y, goal_x, goal_y):
    """Calculates the angle from the robot to the goal."""
    return math.atan2(goal_y - robot_y, goal_x - robot_x)

def plot_robot_path(path, obstacle, start, goal):
    """
    Creates and displays a plot of the robot's path, the world,
    the obstacle, and start/goal points.
    """
    x_coords, y_coords = zip(*path)
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the main simulation elements
    ax.plot(x_coords, y_coords, 'b-', label='Robot Path')
    ax.plot(start[0], start[1], 'go', markersize=10, label='Start')
    ax.plot(goal[0], goal[1], 'r*', markersize=15, label='Goal')
    obstacle_patch = patches.Rectangle(
        (obstacle['x'], obstacle['y']), obstacle['w'], obstacle['h'],
        facecolor='gray', label='Obstacle'
    )
    ax.add_patch(obstacle_patch)

    # Configure plot appearance
    ax.set_title("Robot Path Simulation")
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_xlim(0, WORLD_X_MAX)
    ax.set_ylim(0, WORLD_Y_MAX)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    ax.legend()

    plt.show()


# --- 3. Main Simulation ---
print("--- Starting Bug Algorithm Simulation ---")

# --- Initialisation ---
x_pos, y_pos = START_POS
heading = 0.0
robot_state = "MOVING_TO_GOAL"
wall_follow_steps_remaining = 0
step_count = 0
MAX_STEPS = 2000

# Store the (x, y) coordinates of the robot's path for plotting later.
path_history = [(x_pos, y_pos)]

# --- Main Loop ---
while calculate_distance(x_pos, y_pos, GOAL_POS[0], GOAL_POS[1]) > GOAL_TOLERANCE:
    # State machine logic to determine robot behavior.
    if robot_state == "MOVING_TO_GOAL":
        angle_to_goal = calculate_angle_to_goal(x_pos, y_pos, GOAL_POS[0], GOAL_POS[1])
        if angle_to_goal > heading: left_wheel_speed, right_wheel_speed = 1.8, 2.0
        else: left_wheel_speed, right_wheel_speed = 2.0, 1.8
        next_x, next_y, _ = update_robot_state(x_pos, y_pos, heading, left_wheel_speed, right_wheel_speed)
        if is_colliding(next_x, next_y, OBSTACLE):
            print(f"Step {step_count}: Collision predicted! Switching to WALL_FOLLOWING.")
            robot_state = "FOLLOWING_WALL"
            wall_follow_steps_remaining = 150
            left_wheel_speed, right_wheel_speed = -1.0, 1.0
    elif robot_state == "FOLLOWING_WALL":
        left_wheel_speed, right_wheel_speed = 2.0, 1.7
        next_x, next_y, _ = update_robot_state(x_pos, y_pos, heading, left_wheel_speed, right_wheel_speed)
        if is_colliding(next_x, next_y, OBSTACLE):
            left_wheel_speed, right_wheel_speed = -1.0, 1.0
        wall_follow_steps_remaining -= 1
        if wall_follow_steps_remaining <= 0:
            print(f"Step {step_count}: Wall following complete. Switching to MOVING_TO_GOAL.")
            robot_state = "MOVING_TO_GOAL"

    # --- Update state and record history ---
    x_pos, y_pos, heading = update_robot_state(x_pos, y_pos, heading, left_wheel_speed, right_wheel_speed)
    path_history.append((x_pos, y_pos))

    step_count += 1
    if step_count >= MAX_STEPS:
        print("SAFETY: Maximum steps reached.")
        break

# --- 4. Final Analysis & Visualisation ---
print("\n--- Simulation Finished ---")
final_dist = calculate_distance(x_pos, y_pos, GOAL_POS[0], GOAL_POS[1])
if final_dist <= GOAL_TOLERANCE:
    print(f"Result: Success! Reached goal in {step_count} steps.")
else:
    print(f"Result: Failure. Stopped {final_dist:.2f}m from the goal.")

# Display the final path.
plot_robot_path(path_history, OBSTACLE, START_POS, GOAL_POS)
