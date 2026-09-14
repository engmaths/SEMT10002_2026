'''
================
Exercise 2
================
1. The following table contains data from a recent assessment. 
Make some lists to store this data (one list per question) and 
then write a loop to calculate the average mark for each question. 

Student   Question 1  Question 2  Question 3 
Martin    6           1           4 
Arthur    3           8           4 
Hemma     7           4           5 
Josh      4           7           3 
'''

question1_marks = [6, 3, 4, 7]
question2_marks = [1, 8, 4, 7]
question3_marks = [4, 4, 5, 3]

for ii in [question1_marks, question2_marks, question3_marks]:

    total = 0

    for mark in ii:

        # Cumulatively add the marks for the question
        total += mark

    # Find the average for the question
    average = total / len(ii)

    print(average)



'''
2a. Write a loop to calculate the sum of the values in 3 x 3 matrices. 
What is the sum of the values in the matrix below?

5 3 4
3 4 2
4 3 1
'''

matrix = [[5, 3, 4],
          [3, 4, 2],
          [4, 3, 1]]

total = 0

for ii in matrix:
    for jj in ii:
        total += jj

print(total)

'''
2b. Write a loop that replaces each value in a matrix with its square. 
i.e the top left value (5) should be replaced with 5^2=25 and so on.
'''

for ii in matrix:
    for jj in range(len(ii)):
        ii[jj] = ii[jj]**2
print(matrix)


'''
4. Write some code that given a list of numbers will create a new list where each element 
is the cumulative sum of numbers in the first list. 

I.e if we have the list of numbers 
list_of_numbers = [1, 3, 6, 10], 
then our code should create a new list
cumulative_sum = [1, 4, 10, 20]
'''

list_of_numbers = [1, 3, 6, 10]

number_to_append = 0
cumulative_sum = []

for ii in list_of_numbers:
    number_to_append += ii
    cumulative_sum.append(number_to_append)

print(cumulative_sum)