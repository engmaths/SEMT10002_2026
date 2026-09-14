'''
================
Exercise 2
================

The number of cyclists crossing a bridge at hourly intervals during a 24 hour period was recorded every day for 1 year.

The data recorded during each 1 hour interval throughout the day was averaged for all days of the year.

The data shows the number of cyclist travelling:
    - east
    - west
    - in total

Import this data from `hourly_cycle_count_weekend.csv`.

Create a scatter plot of the three sets of data, with 'Time' on the horizontal axis and 'Number of cyclists' on the vertical axis.
'''

from matplotlib import pyplot as plt
import csv

with open('hourly_cycle_count_weekend.csv') as file:

    data = csv.reader(file)
    
    data = list(data)

    print(data)
    
    time, east, west, total = [], [], [], []
    
    # Store data from each row excluding the column headings
    for row in data[1:]:

        # Hour
        time.append(int(row[0][:2]))

        # Cyclists going east
        east.append(float(row[1]))

        # Cyclists goin west
        west.append(float(row[2]))

        # Total cyclists
        total.append(float(row[3]))
    
    # Generate scatter plot of each data series
    plt.plot(time, east, 'o')
    plt.plot(time, west, 'o')
    plt.plot(time, total, 'o')
    
    # Label axes
    plt.xlabel('Time')
    plt.ylabel('Average number of cyclists')
    plt.show()
