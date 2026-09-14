'''
====================
Exercise 1
====================

1. Import the file rainfall.csv
2. Compute:
    - the total annual rainfall 
    - the average monthly rainfall
    - the maximum and minimum monthly rainfall 

'''

import csv

with open('rainfall.csv') as file:

    reader = csv.reader(file)

    data = list(reader)

rainfall = data[1]

for ii in range(len(rainfall)):
    rainfall[ii] = float(rainfall[ii])

# Convert string representation of rainfall values to numerical data


total_annual_rainfall = sum(rainfall)
average_monthly_rainfall = total_annual_rainfall / len(rainfall)
maximum_monthly_rainfall = max(rainfall)
minimum_monthly_rainfall = min(rainfall)

print('total annual rainfall:', total_annual_rainfall)
print('the average monthly rainfall:', average_monthly_rainfall)
print('the maximummonthly rainfall:', maximum_monthly_rainfall)
print('the minimum monthly rainfall:', minimum_monthly_rainfall)