# --- Consolidation Exercise: Model Answer ---
#
# Goal: Implement a simple "Bug Algorithm" navigator using a state machine.
#       The robot moves towards a goal and follows obstacles upon collision
#       for a fixed duration before re-attempting its goal path.
#

import math

# --- 1. Simulation Setup ---
# World, Robot Constants, and Mission Parameters
WORLD_X_MAX = 100.0
WORLD_Y_MAX = 100.0
WHEELBASE = 0.5
TIME_STEP = 0.1

# A single, large obstacle for navigation.
OBSTACLE = {'x': 30.0, 'y': 30.0, 'w': 20.0, 'h': 40.0}

# Mission start, goal, and success tolerance.
START_POS = (10.0, 50.0)
GOAL_POS = (80.0, 50.0)
GOAL_TOLERANCE = 1.5  # Max distance from goal to be considered a success (m).

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
    """Checks if a position collides with world boundaries or a given obstacle."""
    if not (0 <= x <= WORLD_X_MAX and 0 <= y <= WORLD_Y_MAX):
        return True # Out of bounds
    if (obstacle['x'] <= x <= obstacle['x'] + obstacle['w'] and \
        obstacle['y'] <= y <= obstacle['y'] + obstacle['h']):
        return True # Inside obstacle
    return False

def calculate_distance(x1, y1, x2, y2):
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_angle_to_goal(robot_x, robot_y, goal_x, goal_y):
    """Calculates the global angle from the robot to the goal in radians."""
    return math.atan2(goal_y - robot_y, goal_x - robot_x)

# --- 3. Main Simulation ---
print("--- Starting Bug Algorithm Simulation ---")

# --- Initialisation ---
x_pos, y_pos = START_POS
heading = 0.0
robot_state = "MOVING_TO_GOAL"  # State machine variable
wall_follow_steps_remaining = 0

# Loop control
step_count = 0
MAX_STEPS = 2000

# --- Main Loop ---
while calculate_distance(x_pos, y_pos, GOAL_POS[0], GOAL_POS[1]) > GOAL_TOLERANCE:
    # The robot's behaviour is determined by its current state.
    if robot_state == "MOVING_TO_GOAL":
        # Steer towards the goal.
        angle_to_goal = calculate_angle_to_goal(x_pos, y_pos, GOAL_POS[0], GOAL_POS[1])
        # Simple proportional controller: if the goal is to the left of our
        # current heading, turn left, and vice-versa.
        if angle_to_goal > heading:
            left_wheel_speed, right_wheel_speed = 1.8, 2.0 # Turn left
        else:
            left_wheel_speed, right_wheel_speed = 2.0, 1.8 # Turn right

        # Predict next position to check for imminent collision.
        next_x, next_y, _ = update_robot_state(x_pos, y_pos, heading, left_wheel_speed, right_wheel_speed)
        if is_colliding(next_x, next_y, OBSTACLE):
            print(f"Step {step_count}: Collision predicted! Switching to WALL_FOLLOWING.")
            robot_state = "FOLLOWING_WALL"
            wall_follow_steps_remaining = 150 # Set timer for wall-following duration.
            left_wheel_speed, right_wheel_speed = -1.0, 1.0 # Turn sharply away from obstacle.

    elif robot_state == "FOLLOWING_WALL":
        # Simple wall following: drive forward while gently turning right to "hug" the wall.
        left_wheel_speed, right_wheel_speed = 2.0, 1.7

        # If we're about to hit the wall again (e.g. at a corner), turn away sharply.
        next_x, next_y, _ = update_robot_state(x_pos, y_pos, heading, left_wheel_speed, right_wheel_speed)
        if is_colliding(next_x, next_y, OBSTACLE):
            left_wheel_speed, right_wheel_speed = -1.0, 1.0 # Turn left

        # Decrement the wall-following timer.
        wall_follow_steps_remaining -= 1
        if wall_follow_steps_remaining <= 0:
            print(f"Step {step_count}: Wall following timer elapsed. Re-attempting goal.")
            robot_state = "MOVING_TO_GOAL"

    # --- Update state and check loop conditions ---
    x_pos, y_pos, heading = update_robot_state(x_pos, y_pos, heading, left_wheel_speed, right_wheel_speed)
    step_count += 1

    # Log status periodically.
    if step_count % 20 == 0:
        print(f"Step {step_count}: Pos=({x_pos:.1f}, {y_pos:.1f}), State={robot_state}")

    if step_count >= MAX_STEPS:
        print("SAFETY: Maximum steps reached.")
        break

# --- 4. Final Analysis ---
print("\n--- Simulation Finished ---")
final_dist = calculate_distance(x_pos, y_pos, GOAL_POS[0], GOAL_POS[1])
if final_dist <= GOAL_TOLERANCE:
    print(f"Result: Success! Reached goal in {step_count} steps.")
else:
    print(f"Result: Failure. Stopped {final_dist:.2f}m from the goal.")
