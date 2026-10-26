"""
================
Exercise 1
================
The table contains each student's mark for each question in an assessment. 

a. Use a dictionary to represent the table

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
"""

# -------------------------------------------
# a
# -------------------------------------------
all_marks = {   "martin": {1:6,     2:5 ,   3:5},
                "arthur": {1:10,    2:4,    3:6},
                "hemma":  {1:7,     2:2,    3:5},
                "josh":   {1:4,     2:3,    3:3}
            }


# -------------------------------------------
# b
# -------------------------------------------
print("-----------B-----------")

for q in range(1,4):
    total = 0
    for j in all_marks.values():
        total += j[q]
    average = total/len(all_marks)
    print("The average mark for question", q, "is", average)

# -------------------------------------------
# c
# -------------------------------------------
print("-----------C-----------")
totals = (10, 5, 6)

# Approach i - use dictionary method setdefault to add new keys to an empty dictionary
# Take each question
new_table = {}
for q, t in zip(range(1,4), totals):
    for student in all_marks:
        # Update the new table with the student percentage for the question
        percentage = all_marks[student][q] / t * 100
        new_table.setdefault(student, {})
        new_table[student][q]=percentage

print("New table:\n", new_table)
print()

# Approach ii - use dictionary method copy to add new keys to an empty dictionary
new_table = {}
# Take each student
for student in all_marks:

    # Copy the student data from the original dictionary
    new_table[student]=all_marks[student].copy()

    # Update the new table with the student percentage for the question
    for q, t in zip(range(1,4), totals):
        percentage = new_table[student][q] / t * 100
        new_table[student][q]=percentage
print("New table:\n", new_table)     
print()

# -------------------------------------------
# d
# -------------------------------------------
print("-----------D-----------")
assessment_total = sum(totals)

for student, marks in all_marks.items():

    total = sum(marks.values())

    percentage = total/assessment_total * 100

    print(student, "scored", percentage, "%")




