'''
================
Exercise 3
================

1. Given two lists, write some code that will create a new list containing the higher element from each pair of elements in the two lists.
For example, if we have the lists:
list1 = [1, 4, 9]
list2 = [1, 8, 27]
Then our code should create a new list:
higher_elements = [1, 8, 27]        
'''

list1 = [2, 5, 7, 1, 10, 14, 16, 1, 34, 8]
list2 = [6, 3, 27, 3, 9, 12, 15, 2, 30, 5]
higher_elements = []

for ii, jj in zip(list1, list2):
    if ii > jj:
        higher_elements.append(ii)
    else:
        higher_elements.append(jj)

print(higher_elements)

'''
2. Modify your code (if necessary) to work with *any* number of lists. 
For example, if we input three lists your code should create a new list containing the highest element at each index in the three lists.
If we input four lists, your code should create a new list containing the highest element at each index in the four lists, and so on. 
'''
list3 = [1, 8, 3, 4, 5, 6, 7, 8, 9, 10]
higher_elements = []

for ii in zip(list1, list2, list3):
    higher_elements.append(max(ii))

print(higher_elements)