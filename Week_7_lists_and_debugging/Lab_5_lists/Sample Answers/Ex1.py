'''
================
Exercise 1
================
The table contains each student's mark for each question in an assessment. 

a. Use lists to represent the table

Student   Question 1  Question 2  Question 3 
Martin    6           5           5 
Arthur    10          4           6 
Hemma     7           2           5 
Josh      4           3           3 

b. Calculate the average mark for each question

c. If the maximum possible mark for Questions 1, 2 and 3 is 10, 5 and 6 respectively, 
produce a new table that shows each mark as a percentage of the total mark for each 
question.

d. Calculate each student's total score as a percentage of the total possible mark for the assessment

'''
# -------------------------------------------
# a
# -------------------------------------------
martin = [6,5,5]
arthur = [10,4,6]
hemma = [7,2,5]
josh = [4,3,3]
marks = [martin, arthur, hemma, josh] 

marks_by_student = [[6,     5,  5],
                    [10,    4,  6],
                    [7,     2,  5],
                    [4,     3,  3]]

marks_by_question = [[6, 10, 7,  4],
                     [5, 4,  2,  3],
                     [5, 6,  5,  3]]

# -------------------------------------------
# b
# -------------------------------------------
# Approach i - using loops
print("-----------B-----------")
for i, question in enumerate(marks_by_question, start=1):
    average = sum(question)/len(question)
    print("The average mark for question", i, "is", average)
print()

# Approach ii - using nested loops to traverse a nested list
n_students = len(marks_by_student)
n_questions = len(marks_by_student[0])

for question in range(n_questions):
    total = 0
    for student in marks_by_student:
        total += student[question]
    average = total/n_students
    print("The average mark for question", question+1, "is", average)
print()

# Approach iii - using zip to unpack a nested list
for i, j in enumerate(zip(*marks_by_student), start=1):
    average = sum(j)/len(j)
    print("The average mark for question", i, "is", average)
print()


# -------------------------------------------
# c
# -------------------------------------------
print("-----------C-----------")
total_marks = [10, 5, 6]

# Approach i - using nested loops to traverse a nested list
new_table = []
for question, total in zip(marks_by_question, total_marks):
    new_line = []
    for mark in question:
        percentage = mark/total * 100
        new_line.append(percentage)
    new_table.append(new_line)
print("New table:", new_table)

# Approach ii - using nested list comprehension
new_table = [[q/total*100 for q in question] for question, total in zip(marks_by_question, total_marks)]
print("New table:", new_table)

# Approach iii - using nested loops to traverse a nested list
new_table =[]
for student in marks_by_student:
    new_line = []
    for mark, total in zip(student, total_marks):
        new_line.append(mark/total*100)
    new_table.append(new_line)
print("New table:", new_table)

# Approach iv - using nested list comprehension
new_table = [[mark/total*100 for mark, total in zip(student, total_marks)] for student in marks_by_student]
print("New table:", new_table)
print()

# -------------------------------------------
# d
# -------------------------------------------
print("-----------D-----------")
students = ["martin", "arthur", "hemma", "josh"]
assessment_total = sum(total_marks)

# Approach i - using a loop to traverse a list
for student, marks in zip(students, marks_by_student):
    percentage = sum(marks)/assessment_total*100
    print(student, "scored", percentage, "%")
print()

# Approach ii - using a loop with zip function to traverse list items for each student simultaneously
for student, marks in zip(students, zip(*marks_by_question)):
    percentage = sum(marks)/assessment_total*100
    print(student, "scored", percentage, "%")
print()


# Approach iii - using nested loops to traverse a nested list
total_marks_by_student = [0,0,0,0]
n_students = len(total_marks_by_student)

# Find total marks for each stuednt for each question
for question in marks_by_question:
    for i in range(n_students):
        total_marks_by_student[i] += question[i]

# Convert total amrks to percentage for each student
for i,j in zip(total_marks_by_student, students):
    percentage = i/assessment_total*100
    print(j, "scored", percentage, "%")
print()


# Approach iii - using list comprehension
percentages = [sum(student)/assessment_total*100 for student in marks_by_student]
print("Student scores as percentages:", percentages) 







    
    




    










# for ii in [question1_marks, question2_marks, question3_marks]:

#     total = 0

#     for mark in ii:

#         # Cumulatively add the marks for the question
#         total += mark

#     # Find the average for the question
#     average = total / len(ii)

#     print(average)



# '''
# 2a. Write a loop to calculate the sum of the values in 3 x 3 matrices. 
# What is the sum of the values in the matrix below?

# 5 3 4
# 3 4 2
# 4 3 1
# '''

# matrix = [[5, 3, 4],
#           [3, 4, 2],
#           [4, 3, 1]]

# total = 0

# for ii in matrix:
#     for jj in ii:
#         total += jj

# print(total)

# '''
# 2b. Write a loop that replaces each value in a matrix with its square. 
# i.e the top left value (5) should be replaced with 5^2=25 and so on.
# '''

# for ii in matrix:
#     for jj in range(len(ii)):
#         ii[jj] = ii[jj]**2
# print(matrix)


# '''
# 4. Write some code that given a list of numbers will create a new list where each element 
# is the cumulative sum of numbers in the first list. 

# I.e if we have the list of numbers 
# list_of_numbers = [1, 3, 6, 10], 
# then our code should create a new list
# cumulative_sum = [1, 4, 10, 20]
# '''

# list_of_numbers = [1, 3, 6, 10]

# number_to_append = 0
# cumulative_sum = []

# for ii in list_of_numbers:
#     number_to_append += ii
#     cumulative_sum.append(number_to_append)

# print(cumulative_sum)