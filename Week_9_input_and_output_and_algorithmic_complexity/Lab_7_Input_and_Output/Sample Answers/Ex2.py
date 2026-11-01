'''
================
Exercise 2
================
1. Import the file input.csv, which contains columns a, b, and c 
(representing coefficients of a quadratic equation ax^2 + bx + c = 0

2. For each row:
    - Calculate the discriminant
    - Compute the real roots if they exist using the quadratic formula

3. Write the results to an output CSV file with columns: a, b, c, discriminant, roots
If the discriminant is negative, write "No real roots" in the root columns.
'''
import csv
from math import sqrt

with open('input.csv') as file:

    data = csv.reader(file)

    data_list = list(data)

# Remove the heading from each column
numerical_data = data_list[1:]

# Convert string data in each row to numerical data
for ii in numerical_data:

    for jj, kk in enumerate(ii):

        ii[jj] = int(kk)

# Compute discriminant and roots for each row
discriminant = []
roots = []

for ii in numerical_data:

    a = ii[0]
    b = ii[1]
    c = ii[2]

    # Compute discriminant
    D = b**2 - 4*a*c

    # Add discriminant to end of row
    ii.append(D)

    # Compute roots
    if D < 0:
        # Add roots to end of row
        ii.append("No real roots")

    else:
        root_1 = -b + sqrt(D) / (2 * a)
        root_2 = -b - sqrt(D) / (2 * a)
        roots_string = str(root_1) + ', ' + str(root_2)

        # Add roots to end of row
        ii.append(roots_string)

    # Save data to output file
    with open('output.csv', 'w') as file:

        writer = csv.writer(file)

        writer.writerows(numerical_data)







