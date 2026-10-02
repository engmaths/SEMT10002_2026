'''
Lots of robots use light sensors to detect and follow marker lines on the floor.  
Consider a robot with three sensors, one on the centreline and one on either side.  
A sensor returns `True` if it is over a line and `False` otherwise.  The useful combinations are:

| Left sensor | Middle sensor | Right sensor | Meaning |
| ---- | ---- | ---- | ---- |
| False | True | False | Centred on line: drive straight |
| True | True | False | Line is slightly to my left: turn left |
| False | True | True | Line is slightly to my right: turn right |
| True | False | False | Line is far to my left: slow and turn left |
| False | False | True | Line is far to my right: slow and turn right |

We'd like you to write some code to tell the robot what to do for a certain sensor reading. 
Your function should take the three sensor readings as input and return a string telling the robot what to do.

We've included some test functions to check whether your code is correct. But these don't cover all examples. 
You should: 
    1. Add additional test functions to cover all the cases. 
    2. Write the function follow_line(left_sensor, middle_sensor, right_sensor) such that it passes all tests.
'''

# Complete this function *after* you've added test functions. 
def follow_line(left_sensor, middle_sensor, right_sensor):

    '???'

#Tests -- only partially complete. Write the remaining tests before working on the function.
if follow_line(False, True, False) == "drive straight":
    print("Test 1 passed")
else:
    print("Test 1 failed")

if follow_line(True, True, False) == "turn left":
    print("Test 2 passed")
else:
    print("Test 2 failed")
