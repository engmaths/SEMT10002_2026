# =============================================================================
# Exercise 5 - Branchless programming
# =============================================================================
#
# This exercise is aimed at students arriving with prior programming
# experience. Unlike Exercises 1-4, you may use any Python syntax you like --
# except for "if" statements. To be clear:
#
#     NO if STATEMENTS. No if, no else, no syntatic equivalents!
#
# Commonly used functions like max() or abs() would generally be implemented
# using an if statement, e.g.
#
#     def max(a, b):
#         if a > b:
#             return a
#         else:
#             return b
#
# However, it turns out that we don't actually need if statements -- instead we
# can just use arithmetic and comparison operations. Code written this way is
# called "branchless", and it's a real programming approach: GPUs, for example,
# use branchless programming to keep thousands of calculations properly
# synchronised.
#
# The key trick: in Python, True and False behave as 1 and 0 in arithmetic. Run
# the warm-up below and make sure you understand it.
#
# Your task is to use branchless programming to implement these functions:
#
#   - maximum(a, b), minimum(a, b) -- the greater (lesser) of a and b.
#   - absolute(x) -- the absolute value of x.
#   - sign(x)     -- the sign of x.
#   - clip(x)     -- clips x to the range [-1, 1]. If x > 1, clip(x) = 1;
#                    if x < -1, clip(x) = -1; in between, clip(x) = x.
#   - median(a, b, c) -- the median value of three numbers.
# =============================================================================

# --- Warm-up (just run and understand this) --------------------------

print(True * 7)        # 7
print(False * 7)       # 0
print((3 > 2) * 10)    # 10, because (3 > 2) is True, which is 1
print((3 > 2) + (2 > 3))  # 1


# To "pick" one of two values without a branch, multiply each value by a
# condition that is 1 when you want it and 0 when you don't, and add.
# Exactly one of the two conditions below is 1 at a time:

def choose(a, b, condition):
    'Returns a if condition is True, otherwise b -- with no if!'
    return a * condition + b * (condition == False)

print(choose(10, 20, 3 > 2))   # 10
print(choose(10, 20, 2 > 3))   # 20


# Your task: implement each function below using branchless programming only
# (no if, no else). Replace 'pass' with your code.

def maximum(a, b):
    # Your code here
    pass

def minimum(a, b):
    # Your code here
    pass

def absolute(x):
    # Your code here
    pass

def sign(x):
    # Your code here
    pass

def clip(x):
    # Your code here
    pass

def median(a, b, c):
    # Your code here
    pass
