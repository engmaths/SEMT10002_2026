'''
================
Exercise 3
================

1. Import the file xyz_data.csv 

2. Print the (x,y,z) coordinates of each row in the file

3. Compute the distance, d, to each point from the previous point
(for the first point compute the distance from (0,0,0))

4. Save the results into a new CSV file called results.csv with columns: x, y, z, magnitude

5. Modify your code to read the file name passed as a command-line argument. 
Include a check that avoids the program exiting with an error if no command line arguments 
or the incorrect number of command line arguments are passed. 
'''
from math import sqrt
import csv 
import sys

if len(sys.argv) != 2:
    print('Usage: python3 Ex3.py <input_file>')
    sys.exit()

else:
    filename = sys.argv[1]

# with open('xyz_data.csv', encoding="utf-8-sig") as file:
with open(filename, encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    data = list(reader)

# Separate data types
header = data[0]
coordinates = data[1:]

# Convert numerical values to numerical data
for ii in coordinates:
    print(ii)
    for jj, kk in enumerate(ii):
        ii[jj] = int(kk)

position = [0, 0, 0]
# Compute the magnitude
for ii in coordinates:

    distance = sqrt((ii[0] - position[0])**2 +
                    (ii[1] - position[1])**2 +
                    (ii[2] - position[2])**2)
    
    # Add distance to data
    ii.append(round(distance, 3))

with open('results.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(coordinates)


    

