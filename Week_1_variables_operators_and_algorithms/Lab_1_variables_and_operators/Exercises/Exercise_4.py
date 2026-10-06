# =============================================================================
# Exercise 4 - Boolean Grade Assignment
# =============================================================================
#
# At the University of CPA, we use the standard university grading scheme:
#
#     Grade      Classification
#     -----      --------------
#     70+        First
#     60-69      2.1
#     50-59      2.2
#     40-49      3rd
#     under 40   Fail
#
# The "grade" used to calculate your classification is a weighted average of
# the marks for the two assignments - the first worth 20% and the second worth
# 80%.
#
# Write some code that uses Boolean expressions to determine the following
# students' overall classification:
#
#     Student   Assignment 1   Assignment 2
#     -------   ------------   ------------
#     Martin    100            35
#     Arthur    40             65
#     Hemma     25             80
#     Josh      60             45
# =============================================================================

# Example: Martin
a1 = 100
a2 = 35

# Only one of these expressions should be true.
is_first = False  # your code here
is_2_1   = False  # your code here
is_2_2   = False  # your code here
is_third = False  # your code here
is_fail  = False  # your code here

print(is_first, is_2_1, is_2_2, is_third, is_fail)
