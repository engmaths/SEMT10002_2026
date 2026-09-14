'''
================
Exercise 4
================

Write a program that:

1. Accepts multiple command-line arguments: 
        python3 filepath <input_file> <output_file> <operation>

        <input_file> : the name of a CSV file containing numeric data.    
        <output_file> : the name of the file to save the results.
        <operation> : a mathematical operation to perform on each column (sum, mean, or standard deviation). 

    Example terminal command:
        python3 Ex4.py xyz_data.csv results.csv mean

2. Imports the file xyz_data.csv 

3. Performs the specified operation on each column of xyz_data.csv 

4. Writes the results to the output CSV file in the format 
Column,Operation,Result
x,mean,5.5
y,mean,302.5
z,mean,10.5

'''
import sys
import csv
from math import sqrt

def compute_mean(my_list):
    return sum(my_list)/len(my_list)

def compute_std(my_list):
    mean = compute_mean(my_list)

    cumulative_sum = 0
    for ii in my_list:
        cumulative_sum += (ii - mean)**2

        variance = cumulative_sum / len(my_list)

        return sqrt(variance)

# 1. Check command-line arguments
if len(sys.argv) < 4:
    print('Usage: python3 Ex4.py <input_file> <output_file> <operation>')
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
operation = sys.argv[3].lower()

if operation not in ["sum", "mean", "std"]:
    print("Error: operation must be 'sum', 'mean', or 'std'")
    sys.exit(1)

# 2. Read data from CSV
with open(input_file, encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    data = list(reader)

# Separate data types
header = data[0]
coordinates = data[1:]

# Convert numerical values to numerical data
for ii in coordinates:
    # print(ii)
    for jj, kk in enumerate(ii):
        ii[jj] = int(kk)

# 3. Perform the chosen operation
x, y, z, results = [], [], [], []

for ii in coordinates:
    x.append(ii[0])
    y.append(ii[1])
    z.append(ii[2])

if operation == "sum":
    for ii in [x,y,z]:
        results.append(sum(ii))

elif operation == "mean":
    for ii in [x,y,z]:
        results.append(compute_mean(ii))

elif operation == "std":
    for ii in [x,y,z]:
        results.append(compute_std(ii))

output_data = [['Column', 'Operation', 'Result']]

for ii, jj in zip(['x', 'y', 'z'], results):
    output_data.append([ii, operation, jj])

# Save results to output CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_data)

