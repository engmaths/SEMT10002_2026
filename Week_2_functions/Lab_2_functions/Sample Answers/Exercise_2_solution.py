# =============================================================
# Exercise 2 - Collision detection
# =============================================================
#
# Part 1
# ======
# In week 1, you wrote code to test whether a point at (x, y) lies
# within radius R of a point (u, v), using only arithmetic and
# comparison operators (no square root!). To reuse it for a
# different obstacle you had to copy, paste and edit. This week we
# can do better by packaging it as a function.
#
# Write a function is_colliding(x, y, u, v, R) that returns True if
# the point (x, y) lies within radius R of the point (u, v), and
# False otherwise. Include a docstring. You should not need the
# square root function - reuse your week 1 approach.
#
# Test it against the same two cases as last week:
#   Robot centred at (0, 0), radius 82.5 mm, obstacle at (50, 60) -> True
#   Robot centred at (0, 0), radius 82.5 mm, obstacle at (70, 60) -> False
#
# Part 2
# ======
# In practice, obstacles are likely to have radii themselves. Two
# *circles* have collided if the distance between their centres is
# less than the sum of their radii. Write a second function that
# returns a boolean for this case. Do you need to change the number
# of inputs / outputs for this function?
#
# Test cases (robot at (0, 0), radius 82.5 mm):
#   Obstacle circle at (100, 50), radius 40 mm -> True
#   Obstacle circle at (100, 50), radius 20 mm -> False
# =============================================================

# Your code here
def is_colliding(x, y, R, u, v):
    '''
    Returns true is the point (x, y) is within the radius R of the point (u, v)
    '''
    return (x-u)**2 + (y-v)**2 < R**2

print(is_colliding(0, 0, 82.5, 50, 60))
print(is_colliding(0, 0, 82.5, 70, 60))

def is_colliding_obstacle(x, y, R_robot, u, v, R_obstacle):
    '''
    Returns true if the circles (x, y, R1) and (u, v, R2) overlap
    '''
    return (x-u)**2 + (y-v)**2 < (R_robot+R_obstacle)**2

print(is_colliding_obstacle(0, 0, 82.5, 100, 50, 40))
print(is_colliding_obstacle(0, 0, 82.5, 100, 50, 20))