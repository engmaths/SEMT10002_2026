# =============================================================================
# Exercise 3 - Collision Detection
# =============================================================================
#
# In robotics, we often need to know whether two objects have collided. A
# simple approach is to model each object as a circle: if the distance between
# their centres is less than the sum of their radii, they have collided.
#
# For now, consider the simpler case: a single point and a circle. A point at
# (x, y) lies inside a circle centred at (u, v) with radius R if:
#
#     sqrt((x - u)**2 + (y - v)**2) < R
#
# Unfortunately, we haven't introduced a square root function yet. Your task is
# to rewrite this condition so that it can be evaluated using only the
# arithmetic and comparison operators covered this week.
#
# Test your solution on the two cases below. Each should print a single boolean
# value.
#
#   Test case 1:
#     Robot centred at (0, 0) with radius 82.5 mm.
#     Obstacle at (50, 60) mm.
#     Expected output: True
#
#   Test case 2:
#     Robot centred at (0, 0) with radius 82.5 mm.
#     Obstacle at (70, 60) mm.
#     Expected output: False
#
# Without using the square root function, complete the code below to test
# whether the point (x, y) is within radius R of point (u, v).
# =============================================================================

# Robot parameters
u = 0       # robot x position (mm)
v = 0       # robot y position (mm)
R = 82.5    # robot body radius (mm)

# Test case 1
x = 50      # obstacle x position (mm)
y = 60      # obstacle y position (mm)
# Your code here

# Test case 2
x = 70
y = 60
# Your code here
