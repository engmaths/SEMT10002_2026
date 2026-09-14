'''
================
Exercise 4
================

1. Square numbers are defined as the numbers n^2 where n is an integer. 
Write some code to create a list of all square numbers below 1000. 
How many are there? What is the largest number below 1000?

2. Triangular numbers T_n are  given by the formula $T_n = n(n+1)/2$.  
Write some code to create a list of all triangular numbers below 1000. 
How many are there? What is the largest number below 1000?

3. Write some code to count how many square numbers (below 1000) are also triangular numbers.
'''

'''
Create a list of all SQUARE numbers below 1000. 
How many are there? 
What is the largest number below 1000?
'''
squares_below_1000 = []
counter = 0

while True:
    counter += 1
    square = counter**2
    if square < 1000:
        squares_below_1000.append(square)
    else:
        break

print('There are', len(squares_below_1000), 'square numbers below 1000')
print('The largest is', squares_below_1000[-1])


'''
Create a list of all TRIANGULAR numbers below 1000. 
How many are there? 
What is the largest number below 1000?
'''

triangular_below_1000 = []
counter = 0

while True:
    counter += 1
    triangular = counter * (counter + 1)/2
    if triangular < 1000:
        triangular_below_1000.append(triangular)
    else:
        break

print('There are', len(triangular_below_1000), 'triangular numbers below 1000')
print('The largest is', triangular_below_1000[-1])
print(triangular_below_1000)


'''
Count how many square numbers (below 1000) are also triangular numbers
'''

triangular_and_square = []

for ii in squares_below_1000:
    if ii in triangular_below_1000:
        triangular_and_square.append(ii)

print(triangular_and_square)






