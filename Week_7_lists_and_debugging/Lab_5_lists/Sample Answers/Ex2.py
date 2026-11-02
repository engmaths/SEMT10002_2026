'''
================
Exercise 2
================

(a) The function given below should return a new list containing the sum of every k 
consecutive values in a list.
Every litem in the new list must be the sum of k values. 
Find and fix the problem with the current function, so that it handles boundary index 
values (the first and last item(s) in a list) correctly.
Fix the function so that it handles boundary index values (the first and last item(s) 
in a list) correctly.
Check that it can handle different values of k.

(b) A moving average filter is used in signal processing for smoothing data
It returns the average of every N consecutive values in a sequence. 
Modify the function so that it returns the average of every k consecutive values in a 
list, instead of the total. 

(c) A robot has a 360° LiDAR scanner producing one distance measurement every 10°. 
To apply a 3 point moving average, for example, the mean of the readings at 350°, 0°, and 
10° must be calculated. 
Assuming the reading at 0° is the first value in the list and 350° is the last, wraparound 
boundary conditions are needed. 
Wraparound boundary conditions:
- If the index is the last in the sequence, its upper neightbour is the first in the sequence 
- If the index is the first in the sequence, its lower neighbour is the last in the sequence

Modify your function so that it applies wraparound boundary conditions 
       
'''

def filter(xs, k):

    totals = []
    
    for i in range(len(xs)):
        
        print(xs[i:i+k]) # Shows the issue

        total = sum(xs[i:i+k])
        
        totals.append(total)

    return totals

totals = filter([1,2,3,4,5,6,7,8,9], 3)
print(totals)
print()

# -------------------------------------------
# a
# -------------------------------------------

def filter_fixed(xs, k):

    totals = []
    
    # for i in range(len(xs)): # This line fixed 
    for i in range(len(xs) - k + 1):

        # print(xs[i:i+k]) 

        total = sum(xs[i:i+k])
        
        totals.append(total)

    return totals

totals = filter_fixed([1,2,3,4,5,6,7,8,9], 3)
print(totals)

# -------------------------------------------
# b
# -------------------------------------------
def filter_average(xs, k):

    means = []
    
    for i in range(len(xs) - k + 1):

        # print(xs[i:i+k]) 

        total =sum(xs[i:i+k])

        mean = total/k
        
        means.append(mean)

    return means

means = filter_average([1,2,3,4,5,6,7,8,9], 3)
print(means)


# -------------------------------------------
# c
# -------------------------------------------

# Approach i
def filter_wraparound(xs, k):

    means = []

    for i in range(len(xs)):

        total = sum(xs[i:i+k])

        # If index out of range, takes values form the starts of the list
        if i+k > len(xs):
            difference = int(i+k - len(xs))
            total += sum(xs[:difference])

        mean = total/k
        
        means.append(mean)

    return means

means = filter_wraparound([1,2,3,4,5,6,7,8,9], 3)
print(means)

# Approach ii - Use modulo operator to get wraparound indexes
def filter_wraparound(xs, k):

    means = []

    for i in range(len(xs)):

        total = 0

        for j in range(k):
            index = (i+j) % len(xs)
            total += xs[index]

        mean = total/k
        
        means.append(mean)

    return means

means = filter_wraparound([1,2,3,4,5,6,7,8,9], 3)
print(means)