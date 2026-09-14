'''
================
Exercise 4
================

Your robotics team is developing a simple data management system to keep track of a fleet of *mobile* robots working in a warehouse.

Each robot has:
- a unique ID
- a position in 2D space (x, y)
- a battery level (%)
- a status (e.g. "idle", "moving", "charging")
- a set of task statistics (e.g. number of deliveries completed)

Import the file robot_fleet_data.csv and design a data structure using tuples and dictionaries to represent this information.
(Hint: Use the function `csv.DictReader()` from the `csv` module to read the data from the file into a dictionary structure)
- Which parts should be immutable (tuples)?
- Which parts should be mutable (dictionaries)?
There is no right or wrong answer here! 

Your program should:
- Print the current position of robot R002.
- Update R002’s status to "charging".
- Increase R003’s delivery count by 1.
- Add a new robot, R004 at position (7.5, 2.0) with 100% battery and status "idle".
'''
import csv

fleet = {}

# Read from CSV
with open("robot_fleet_data.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

        robot_id = row["Robot ID"]

        # Create position as an immutable tuple
        x = float(row["Position x"])
        y = float(row["Position y"])
        position = (x, y)

        # Build robot record as dictionary (mutable fields)
        fleet[robot_id] = {"position": position,
                           "battery": int(row["Battery (%)"]),
                           "status": row["Status"],
                           "deliveries": int(row["Deliveries"])
                           }

# Print position of robot R002
print("R002 position:", fleet["R002"]["position"])

# Update R002’s status to "charging"
fleet["R002"]["status"] = "charging"

# Increase R003’s deliveries by 1
fleet["R003"]["deliveries"] += 1

# Add new robot R004
fleet["R004"] = {
    "position": (7.5, 2.0),
    "battery": 100,
    "status": "idle",
    "deliveries": 0,
}

print("Updated fleet:")
for robot, data in fleet.items():
    print(robot, data)

