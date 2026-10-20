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
