'''
====================
Exercise 1
====================

1. Make two lists containing the values [1, 4, 9] and [1, 8, 27].
2. Make a nested list that contains both lists.
3. Double the value of the first element in each list.
4. Find the sum of the first element of the first list and the last element of the second list.
5. Add the first element of the first list to the end of the second list.

'''

# Make two lists containing the values [1, 4, 9] and [1, 8, 27]
list1 = [1, 4, 9]
list2 = [1, 8, 27]

# Make a nested list that contains both lists
nested_list = [list1, list2]
print(nested_list)

# Double the value of the first element in each list
for ii in nested_list:
    ii[0] = 2*ii[0]
print(list1, list2)

# Find the sum of the first element of the first list and the last element of the second list
sum_of_elements = list1[0] + list2[-1]
print(sum_of_elements)

# Add the first element of the first list to the last element of the second list
list2.append(list1[0])
print(list2)





