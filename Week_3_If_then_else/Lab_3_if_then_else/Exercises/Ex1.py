'''
## Exercise 2 - Circles

Suppose we have three circles in the $xy$-plane:

- Circle $C_1$ is centred at $(0, 0)$ with radius of length 5.
- Circle $C_2$ is centred at $(2, 1)$ and has radius of length 2.
- Circle $C_3$ is centred at $(-5, 0)$ and has a radius of length 3.

The image here (https://raw.githubusercontent.com/engmaths/SEMT10002_2025/refs/heads/main/media/week_2/circles.png) illustrates the arrangement.

> Using conditional statements, write a function which takes in the variables $x$ and $y$ and tells the user which circle(s) the point $(x, y)$ is in.

> Think about the order in which your program evaluates the expressions? Is this the most efficient way to structure the code?
'''

circle1_centre_x = 0
circle1_centre_y = 0
circle1_radius = 5

circle2_centre_x = 2
circle2_centre_y = 1
circle2_radius = 2

circle3_centre_x = -5
circle3_centre_y = 0
circle3_radius = 3

def is_inside_circles(x, y):

    'Put your code here'
    return None


#Dont change these -- just run them and use them to check your code is correct.
print("Running tests")
print("=============")

if is_inside_circles(0, 0) == "1":
    print("Test 1 passed")
else:
    print("Test 1 failed")

if is_inside_circles(2, 0) == "1, 2":
    print("Test 2 passed")
else:
    print("Test 2 failed")

if is_inside_circles(-6, -1) == "3":
    print("Test 3 passed")
else:
    print("Test 3 failed")

if is_inside_circles(-3, 1) == "1, 3":
    print("Test 4 passed")
else:
    print("Test 4 failed")

if is_inside_circles(-10, -10) == None:
    print("Test 5 passed")
else:
    print("Test 5 failed")