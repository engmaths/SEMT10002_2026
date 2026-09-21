# --- Week 1: Model Answer ---
#
# Goal: Define the robot's state and simulate a single time step forward.
#

import math

# --- 1. Robot Constants ---
WHEELBASE = 0.5  # Distance between the wheels (meters)
TIME_STEP = 0.1  # Simulation time step (seconds)

# --- 2. Initial Robot State ---
x_pos = 10.0      # Initial x-position (meters)
y_pos = 5.0       # Initial y-position (meters)
heading = math.pi / 4  # Initial heading (radians)

# --- 3. Control Inputs ---
# These are fixed for this simple simulation.
# Speeds are set to make the robot turn slightly to the left.
left_wheel_speed = 1.5   # m/s
right_wheel_speed = 1.8  # m/s

# --- 4. Print Initial State ---
print("--- Initial Robot State ---")
print(f"Position: ({x_pos:.2f}, {y_pos:.2f}) meters")
print(f"Heading: {math.degrees(heading):.2f} degrees")
print("-" * 25)

# --- 5. Calculate Velocities from Wheel Speeds ---
# Based on a differential drive kinematic model.
linear_velocity = (left_wheel_speed + right_wheel_speed) / 2
angular_velocity = (right_wheel_speed - left_wheel_speed) / WHEELBASE

# --- 6. Calculate State Change over the Time Step ---
delta_heading = angular_velocity * TIME_STEP
delta_x = linear_velocity * math.cos(heading) * TIME_STEP
delta_y = linear_velocity * math.sin(heading) * TIME_STEP

# --- 7. Update State ---
x_pos += delta_x
y_pos += delta_y
heading += delta_heading

# --- 8. Print Final State ---
print(f"--- Updated Robot State (after {TIME_STEP} seconds) ---")
print(f"Position: ({x_pos:.2f}, {y_pos:.2f}) meters")
print(f"Heading: {math.degrees(heading):.2f} degrees")
print("-" * 25)
