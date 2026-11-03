# --- Week 4: Model Answer ---
#
# Goal: Refactor the robot simulation by organizing the logic into reusable
# functions for state updates, boundary checks, and display.
#

import math

# --- 1. Global Constants ---
# Constants used throughout the simulation.
WORLD_X_MAX = 100.0
WORLD_Y_MAX = 100.0
WHEELBASE = 0.5    # meters
TIME_STEP = 0.1    # seconds

# --- 2. Function Definitions ---

def update_robot_state(x, y, heading, speed_l, speed_r):
    """
    Calculates the new state of the robot after one time step.

    Args:
        x (float): Current x-position.
        y (float): Current y-position.
        heading (float): Current heading in radians.
        speed_l (float): Left wheel speed (m/s).
        speed_r (float): Right wheel speed (m/s).

    Returns:
        tuple: A tuple of (new_x, new_y, new_heading).
    """
    linear_velocity = (speed_l + speed_r) / 2
    angular_velocity = (speed_r - speed_l) / WHEELBASE

    delta_heading = angular_velocity * TIME_STEP
    delta_x = linear_velocity * math.cos(heading) * TIME_STEP
    delta_y = linear_velocity * math.sin(heading) * TIME_STEP

    new_x = x + delta_x
    new_y = y + delta_y
    new_heading = heading + delta_heading

    return new_x, new_y, new_heading

def is_in_bounds(x, y):
    """
    Checks if a given position is within the defined world boundaries.

    Args:
        x (float): The x-position to check.
        y (float): The y-position to check.

    Returns:
        bool: True if the position is in bounds, False otherwise.
    """
    # A more concise way to write this would be:
    # return 0 <= x <= WORLD_X_MAX and 0 <= y <= WORLD_Y_MAX
    if 0 <= x <= WORLD_X_MAX and 0 <= y <= WORLD_Y_MAX:
        return True
    else:
        return False

def display_robot_state(step, x, y, heading):
    """Prints the robot's current state to the console."""
    print(f"Step {step}: Pos=({x:.2f}, {y:.2f}), H={math.degrees(heading):.2f}°")


# --- 3. Main Simulation Loop ---
print("--- Starting Functional Simulation (Goal: x > 90) ---")

# --- Initialisation ---
x_pos = 10.0
y_pos = 10.0
heading = math.pi / 6 # 30 degrees

# Control inputs
left_wheel_speed = 2.0
right_wheel_speed = 1.9

# Loop control
step_count = 0
MAX_STEPS = 1000

# The main loop now clearly shows the high-level logic of the simulation.
while x_pos < 90:
    display_robot_state(step_count, x_pos, y_pos, heading)

    # Check for termination conditions
    if not is_in_bounds(x_pos, y_pos):
        print("EVENT: Robot has gone out of bounds!")
        break

    if step_count >= MAX_STEPS:
        print("SAFETY: Maximum steps reached.")
        break

    # Calculate the next state
    x_pos, y_pos, heading = update_robot_state(
        x_pos, y_pos, heading, left_wheel_speed, right_wheel_speed
    )

    step_count += 1

# --- 4. Post-Simulation Analysis ---
print("\n--- Simulation Finished ---")
print(f"Final Position: ({x_pos:.2f}, {y_pos:.2f}) after {step_count} steps.")

if x_pos >= 90:
    print("Result: Success! The robot reached its goal.")
elif not is_in_bounds(x_pos, y_pos):
    print("Result: Failure. The robot went out of bounds.")
else:
    print("Result: Failure. The simulation stopped for another reason.")
