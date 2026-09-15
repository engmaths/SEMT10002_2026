'''
================
Exercise 3
================

Fix this code

The function should return the neighbouring values around a chosen index in a list: the previous value, the current value, and the next value.

If the index is the last in the sequence, the next value should be the first in the sequence. 

If the index is the first in the sequence, the previous value should be the last in the sequence. 

Fix the function so that it can handle boundary index values (index=0 and index=4) and intermediate index values (e.g. index=2) correctly.  
'''

def get_neighbours(values, index):
    previous = values[index - 1]
    current = values[index]
    next = values[index + 1]

    return [previous, current, next]


numbers = [10, 20, 30, 40, 50]

# Testing function for intermediate index 2
result = get_neighbours(numbers, 2)
print(result)