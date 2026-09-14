# --- Week 3: Model Answer ---
#
# Goal: Simulate robot movement over time using loops, combining the movement
# logic from Week 1 and the boundary checks from Week 2.
#

import math

# --- 1. Simulation Setup ---
# World Boundaries
WORLD_X_MAX = 100.0
WORLD_Y_MAX = 100.0

# Robot Constants
WHEELBASE = 0.5  # meters
TIME_STEP = 0.1  # seconds

# Control Inputs (fixed for these simulations)
left_wheel_speed = 2.0  # m/s
right_wheel_speed = 1.9 # m/s (slight right curve)

# --- Part 1: For-Loop Simulation (Fixed Duration) ---
# Goal: Run the simulation for a fixed number of steps, stopping early
# if the robot goes out of bounds.

print("--- Starting Part 1: For-Loop Simulation (50 steps) ---")

# Initial state for this simulation.
x_pos = 10.0
y_pos = 10.0
heading = math.pi / 6 # 30 degrees

for step in range(50):
    print(f"Step {step+1}: Pos=({x_pos:.2f}, {y_pos:.2f}), H={math.degrees(heading):.2f}°")

    # Boundary check: stop the simulation if the robot leaves the world.
    if not (0 <= x_pos <= WORLD_X_MAX and 0 <= y_pos <= WORLD_Y_MAX):
        print("EVENT: Robot has gone out of bounds! Stopping simulation.")
        break

    # Simulate a "sticky patch": skip movement calculations for one step if in this zone.
    if 40 < x_pos < 45:
        print("INFO: Robot is in a sticky patch! Pausing movement for this step.")
        continue

    # --- Standard Movement Calculation & State Update ---
    linear_velocity = (left_wheel_speed + right_wheel_speed) / 2
    angular_velocity = (right_wheel_speed - left_wheel_speed) / WHEELBASE

    delta_heading = angular_velocity * TIME_STEP
    delta_x = linear_velocity * math.cos(heading) * TIME_STEP
    delta_y = linear_velocity * math.sin(heading) * TIME_STEP

    x_pos += delta_x
    y_pos += delta_y
    heading += delta_heading

print("--- For-Loop Simulation Finished ---")


# --- Part 2: While-Loop Simulation (Goal-Oriented) ---
# Goal: Run the simulation until the robot's x-position exceeds 90.

print("\n\n--- Starting Part 2: While-Loop Simulation (Goal: x > 90) ---")

# Reset robot state for the new simulation.
x_pos = 10.0
y_pos = 10.0
heading = math.pi / 6

# A safety counter to prevent an infinite loop if the goal is unreachable.
step_count = 0
MAX_STEPS = 1000

while x_pos < 90:
    # Conditions to terminate the loop must be checked first.
    if not (0 <= x_pos <= WORLD_X_MAX and 0 <= y_pos <= WORLD_Y_MAX):
        print("EVENT: Robot has gone out of bounds! Stopping simulation.")
        break

    if step_count >= MAX_STEPS:
        print("SAFETY: Maximum steps reached. Stopping simulation.")
        break

    # --- Standard Movement Calculation & State Update ---
    linear_velocity = (left_wheel_speed + right_wheel_speed) / 2
    angular_velocity = (right_wheel_speed - left_wheel_speed) / WHEELBASE
    delta_heading = angular_velocity * TIME_STEP
    delta_x = linear_velocity * math.cos(heading) * TIME_STEP
    delta_y = linear_velocity * math.sin(heading) * TIME_STEP

    x_pos += delta_x
    y_pos += delta_y
    heading += delta_heading
    step_count += 1

    # Log status periodically to avoid flooding the console.
    if step_count % 10 == 0:
        print(f"Step {step_count}: Pos=({x_pos:.2f}, {y_pos:.2f})")


# --- Analysis of While-Loop Outcome ---
# Check the final state to determine if the simulation succeeded or failed.
print("\n--- While-Loop Simulation Finished ---")
print(f"Final Position: ({x_pos:.2f}, {y_pos:.2f}) after {step_count} steps.")

if x_pos >= 90:
    print("Result: Success! The robot reached its goal.")
elif not (0 <= x_pos <= WORLD_X_MAX and 0 <= y_pos <= WORLD_Y_MAX):
    print("Result: Failure. The robot went out of bounds before reaching the goal.")
else:
    print("Result: Failure. The simulation stopped for another reason (e.g., max steps).")
