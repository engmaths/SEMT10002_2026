# --- Week 8: Object-Oriented Refactor ---
#
# Goal: An object-oriented implementation of the robot simulation,
#       encapsulating logic and data within `Robot` and `World` classes
#       for a more modular and maintainable design.
#

import math
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Standalone Utility Functions ---
# Generic math functions that are not specific to a single class.
def calculate_distance(x1, y1, x2, y2):
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# --- Class Definitions ---

class World:
    """
    Represents the simulation environment, including boundaries and obstacles.
    Loads its configuration from a specified map file upon initialization.
    """
    def __init__(self, filepath):
        print(f"Loading world from {filepath}...")
        self.obstacles = []
        self.x_max = 0
        self.y_max = 0
        self.start_pos = (0, 0)
        self.goal_pos = (0, 0)
        self.goal_tolerance = 1.5
        self._load_from_txt(filepath) # Parse the file to populate world attributes.

    def _load_from_txt(self, filepath):
        """Internal method for parsing the map file. Not intended for external use."""
        with open(filepath, 'r') as f:
            for line in f:
                clean_line = line.strip()
                if not clean_line or clean_line.startswith('#'): continue
                parts = clean_line.split()
                keyword = parts[0].lower()
                values = [float(v) for v in parts[1:]]
                if keyword == 'size': self.x_max, self.y_max = values
                elif keyword == 'start': self.start_pos = tuple(values)
                elif keyword == 'goal': self.goal_pos = tuple(values)
                elif keyword == 'obstacle':
                    self.obstacles.append({'x': values[0], 'y': values[1], 'w': values[2], 'h': values[3]})
        print("World loaded successfully.")

    def is_colliding(self, x, y):
        """Checks if a given (x, y) position is out of bounds or inside any obstacle."""
        if not (0 <= x <= self.x_max and 0 <= y <= self.y_max):
            return True
        for obs in self.obstacles:
            if (obs['x'] <= x <= obs['x'] + obs['w'] and obs['y'] <= y <= obs['y'] + obs['h']):
                return True
        return False

class Robot:
    """
    Represents the robot, encapsulating its state (position, heading) and
    movement logic (state machine, kinematics).
    """
    def __init__(self, x=0, y=0, heading=0.0, wheelbase=0.5):
        self.x = x
        self.y = y
        self.heading = heading      # radians
        self.wheelbase = wheelbase  # meters
        self.state = "MOVING_TO_GOAL"
        self.wall_follow_steps_remaining = 0

    def update_state(self, speed_l, speed_r, time_step):
        """Calculates and applies the robot's new position and heading for one step."""
        linear_velocity = (speed_l + speed_r) / 2
        angular_velocity = (speed_r - speed_l) / self.wheelbase
        self.heading += angular_velocity * time_step
        self.x += linear_velocity * math.cos(self.heading) * time_step
        self.y += linear_velocity * math.sin(self.heading) * time_step

    def calculate_angle_to_goal(self, goal_pos):
        """Calculates the absolute angle from the robot to a goal position."""
        return math.atan2(goal_pos[1] - self.y, goal_pos[0] - self.x)

    def predict_next_pos(self, speed_l, speed_r, time_step):
        """
        Calculates the robot's next position without modifying its actual state.
        Used for collision prediction.
        """
        linear_velocity = (speed_l + speed_r) / 2
        angular_velocity = (speed_r - speed_l) / self.wheelbase
        # NOTE: This prediction uses the current heading, not the next one, for simplicity.
        # A more advanced prediction would calculate next_heading first.
        next_x = self.x + linear_velocity * math.cos(self.heading) * time_step
        next_y = self.y + linear_velocity * math.sin(self.heading) * time_step
        return next_x, next_y

# --- Main Execution ---
if __name__ == "__main__":

    # --- 1. Setup ---
    TIME_STEP = 0.1
    MAX_STEPS = 2000

    # Instantiate the World and Robot objects
    try:
        world = World('map.txt')
        robot = Robot(x=world.start_pos[0], y=world.start_pos[1])
    except FileNotFoundError:
        print("Error: map.txt not found. Please ensure it is in the correct directory.")
        exit()

    # --- 2. Simulation Loop ---
    path_history = [(robot.x, robot.y)]
    step_count = 0

    print("Starting simulation...")
    while calculate_distance(robot.x, robot.y, world.goal_pos[0], world.goal_pos[1]) > world.goal_tolerance:

        # Determine wheel speeds based on the robot's state machine
        if robot.state == "MOVING_TO_GOAL":
            angle_to_goal = robot.calculate_angle_to_goal(world.goal_pos)
            speed_l, speed_r = (1.8, 2.0) if angle_to_goal > robot.heading else (2.0, 1.8)

            # Predict collision on the next step
            next_x, next_y = robot.predict_next_pos(speed_l, speed_r, TIME_STEP)
            if world.is_colliding(next_x, next_y):
                robot.state = "FOLLOWING_WALL"
                robot.wall_follow_steps_remaining = 150
                speed_l, speed_r = -1.0, 1.0 # Turn sharply away

        elif robot.state == "FOLLOWING_WALL":
            speed_l, speed_r = 2.0, 1.7 # Hug the wall
            next_x, next_y = robot.predict_next_pos(speed_l, speed_r, TIME_STEP)
            if world.is_colliding(next_x, next_y):
                speed_l, speed_r = -1.0, 1.0 # Turn at corner

            robot.wall_follow_steps_remaining -= 1
            if robot.wall_follow_steps_remaining <= 0:
                robot.state = "MOVING_TO_GOAL"

        # Update the robot object's state using the determined speeds
        robot.update_state(speed_l, speed_r, TIME_STEP)

        # Log data and check loop termination conditions
        path_history.append((robot.x, robot.y))
        step_count += 1
        if step_count >= MAX_STEPS:
            print("Max steps reached.")
            break

    print("Simulation finished.")

    # --- 3. Save results and plot ---
    # NOTE: For larger projects, this plotting function would typically be
    #       moved to a separate 'utils.py' or 'plotting.py' file.
    def plot_simulation(path, world_obj):
        """Generates a plot of the final simulation path and world layout."""
        x_coords, y_coords = zip(*path)
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.plot(x_coords, y_coords, 'b-', label='Robot Path')
        ax.plot(world_obj.start_pos[0], world_obj.start_pos[1], 'go', markersize=10, label='Start')
        ax.plot(world_obj.goal_pos[0], world_obj.goal_pos[1], 'r*', markersize=15, label='Goal')
        for obs in world_obj.obstacles:
            ax.add_patch(patches.Rectangle((obs['x'], obs['y']), obs['w'], obs['h'], facecolor='gray'))
        ax.set_title("Object-Oriented Robot Simulation"), ax.set_xlabel("X Position (m)"), ax.set_ylabel("Y Position (m)")
        ax.set_xlim(0, world_obj.x_max), ax.set_ylim(0, world_obj.y_max)
        ax.set_aspect('equal', adjustable='box'), ax.grid(True), ax.legend()
        plt.show()

    plot_simulation(path_history, world)
