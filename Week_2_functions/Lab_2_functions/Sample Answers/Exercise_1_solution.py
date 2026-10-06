# =============================================================
# Exercise 1 - The average function
# =============================================================
# Part 1
# =======
# Below is a function I have written to take the average of two
# numbers. Use it to find the average of 19315 and 22664.
#
# Part 2
# ======
# Now let's make `average` do some real work. Our robot's centre
# point lies exactly halfway between its two wheels. Suppose the
# left wheel is at position (x=40, y=60) mm and the right wheel is at
# (x=100, y=140) mm. Use the `average` function to compute the
# coordinates of the robot's centre point, and print the result.
#
# Part 3
# ======
# Discussion (with your partner): if you had *four* numbers, would
# average(average(a, b), average(c, d)) give the same answer as
# adding all four and dividing by 4? Would it still work for
# *three* numbers, i.e. average(average(a, b), c)? Try it - and
# remember what week 1 taught you about comparing floats with ==.
# =============================================================


def average(m, n):
    return 0.5 * (m + n)

#  PART 1
print(average(19315, 22664))

#  PART 2
x_average = average(40, 100)
y_average = average(60, 140)
print(x_average, y_average)

# PART 3a
number1 = 1
number2 = 3
number3 = 4
number4 = 5

average_of_averages = average(average(number1, number2), average(number3, number4))
sum_divide = (number1 + number2 + number3 + number4) / 4

print(average_of_averages)
print(sum_divide)
print("Difference is: ", average_of_averages - sum_divide)
print("Numbers are the same:", average_of_averages - sum_divide < 1E-5)

# PART 3b

average_of_averages = average(average(number1, number2), number3)
sum_divide = (number1 + number2 + number3) / 3

print(average_of_averages)
print(sum_divide)
print("Difference is: ", average_of_averages - sum_divide)
print("Numbers are the same:", average_of_averages - sum_divide < 1E-5)