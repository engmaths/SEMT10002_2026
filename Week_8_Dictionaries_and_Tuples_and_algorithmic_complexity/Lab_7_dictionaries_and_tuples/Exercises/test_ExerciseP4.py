from math import pi
from ExerciseP4 import detect_obstacles

# Define map boundaries
map_x_min = 0
map_x_max = 5000
map_y_min = 0
map_y_max = 5000

# Define obstacles: list of ((x, y), (width, height))
obstacles = [
    ((100, 2250), (4000, 500)),    # obstacle 1 
    ((3000, 3000), (800, 1500)),   # obstacle 2
    ((1500, 500), (600, 600))      # obstacle 3
]

def run_test(name, robot_x, robot_y, sensor_angles, sensor_range, expected):
    print(f"Running {name} ... ", end="")

    result = detect_obstacles(
        robot_x,
        robot_y,
        sensor_angles,
        sensor_range,
        obstacles,
        map_x_min=map_x_min,
        map_x_max=map_x_max,
        map_y_min=map_y_min,
        map_y_max=map_y_max
    )

    if result == expected:
        print("PASS")
    else:
        print("FAIL")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")


def main():
    print("\n=== Testing detect_obstacles() ===\n")

    # OBSTACLE DETECTION TESTS  
    run_test(
        "Test 1 — Sensor pointing vertical up towards obstacle 1",
        robot_x=2000, robot_y=2000,
        sensor_angles=[0],  
        sensor_range=300,  
        expected=(True, "obstacle")
    )

    run_test(
        "Test 2 — Sensor pointing horizontal right towards obstacle 3",
        robot_x=1400, robot_y=800,
        sensor_angles=[pi/2],  
        sensor_range=300,
        expected=(True, "obstacle")
    )

    # WALL DETECTION TESTS
    run_test(
        "Test 3 — Sensor pointing left toward left wall",
        robot_x=10, robot_y=2000,
        sensor_angles=[-pi/2],  # LEFT → hits x=0
        sensor_range=300,
        expected=(True, "wall")
    )

    run_test(
        "Test 4 — Sensor pointing  vertical down toward bottom wall",
        robot_x=3000, robot_y=30,
        sensor_angles=[pi], 
        sensor_range=300,
        expected=(True, "wall")
    )

    # NO COLLISION TEST
    run_test(
        "Test 5 — Robot near obstacle 3 but sensor pointing away",
        robot_x=1400, robot_y=800,
        sensor_angles=[-pi/2],  # LEFT, away from obstacle 3
        sensor_range=300,
        expected=(False, None)
    )

    # MULTI-SENSOR TESTS
    run_test(
        "Test 6 — Only right sensor hits obstacle 3",
        robot_x=1400, robot_y=1100,
        sensor_angles=[0, pi/4, pi/2],  # left, up, right → right hits obstacle
        sensor_range=300,
        expected=(True, "obstacle")
    )

    run_test(
        "Test 7 — Robot in open area, no collisions",
        robot_x=3000, robot_y=300,
        sensor_angles=[-pi/4, 0, pi/4],  
        sensor_range=300,
        expected=(False, None)
    )

    run_test(
        "Test 8 — Robot in open area, no collisions",
        robot_x=4000, robot_y=1000,
        sensor_angles=[-pi/4, 0, pi/4],  
        sensor_range=300,
        expected=(False, None)
    )

    print("\n=== Testing complete ===\n")


if __name__ == "__main__":
    main()
