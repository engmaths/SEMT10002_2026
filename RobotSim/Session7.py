# --- Week 7: Unit Tests ---
#
# Goal: A set of unit tests to verify the core mathematical and logical
#       functions of the robot simulation.
#

# Import functions to be tested from the main simulation script.
# Assumes the main script is saved as 'simulation.py'.
from simulation import (
    calculate_distance,
    calculate_angle_to_goal,
    is_colliding,
    update_robot_state
)

import math

# --- Test Suite ---

def test_calculate_distance():
    """Tests the calculate_distance function with known geometric cases."""
    print("Running test: test_calculate_distance...")

    # Test a 3-4-5 right-angled triangle.
    dist = calculate_distance(0, 0, 3, 4)
    assert dist == 5.0, "Failed on 3-4-5 triangle case."

    # Test a simple horizontal line.
    dist = calculate_distance(10, 5, 20, 5)
    assert dist == 10.0, "Failed on horizontal line case."

    print(" -> PASSED")


def test_calculate_angle_to_goal():
    """Tests the atan2-based angle calculation for cardinal and diagonal directions."""
    print("Running test: test_calculate_angle_to_goal...")

    # NOTE: Use math.isclose() for floating-point comparisons to avoid precision errors.

    # Test case 1: Goal is directly to the right (0 radians).
    angle = calculate_angle_to_goal(robot_x=0, robot_y=0, goal_x=10, goal_y=0)
    assert math.isclose(angle, 0.0), "Angle to the right should be 0.0 rad."

    # Test case 2: Goal is directly above (pi/2 radians).
    angle = calculate_angle_to_goal(robot_x=0, robot_y=0, goal_x=0, goal_y=10)
    assert math.isclose(angle, math.pi / 2), "Angle upwards should be pi/2 rad."

    # Test case 3: Goal is at a 45-degree angle (pi/4 radians).
    angle = calculate_angle_to_goal(robot_x=0, robot_y=0, goal_x=5, goal_y=5)
    assert math.isclose(angle, math.pi / 4), "Angle at 45 degrees should be pi/4 rad."

    print(" -> PASSED")


def test_is_colliding():
    """Tests the collision logic for out-of-bounds and in-obstacle cases."""
    print("Running test: test_is_colliding...")

    # Define a simple world fixture for this test.
    test_world = {
        'x_max': 100.0, 'y_max': 100.0,
        'obstacles': [{'x': 20, 'y': 20, 'w': 10, 'h': 10}]
    }

    # Test case 1: A point safely within the world.
    assert not is_colliding(50, 50, test_world), "Safe point should not be colliding."

    # Test case 2: A point out of bounds (x < 0).
    assert is_colliding(-10, 50, test_world), "Out-of-bounds point should be colliding."

    # Test case 3: A point inside the obstacle.
    assert is_colliding(25, 25, test_world), "Point inside obstacle should be colliding."

    print(" -> PASSED")

# TODO: Add a test for the update_robot_state function. This would involve
#       creating a robot dictionary, calling the function, and asserting that
#       the new x, y, and heading values are as expected after one time step.


# --- Test Runner ---
if __name__ == "__main__":
    print("--- STARTING ROBOT SIMULATION TESTS ---")

    try:
        test_calculate_distance()
        test_calculate_angle_to_goal()
        test_is_colliding()

        print("\n======================================")
        print(" ALL TESTS PASSED SUCCESSFULLY! ")
        print("======================================")
    except AssertionError as e:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f" A TEST FAILED: {e}")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
