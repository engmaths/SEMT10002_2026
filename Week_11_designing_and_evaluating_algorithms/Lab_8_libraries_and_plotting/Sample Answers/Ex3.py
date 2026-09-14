'''
================
Exercise 3
================ 

1. Calculate the second moment of area of each beam.
Convert the imported data to different units if needed.  

2. Calculate the natural frequency of each beam:

3. Generate a scatter plot showing natural frequency against the beam density. 

4. There are 4 types of wood in the sample of beams. We can see this as the points are clustered according to their density
Sort the data points into the four types of wood, based on density.
You will need to manually set the threshold values to sort the data 
(Later in the unit we will study algorithms to automate this process of clustering similar data points)
Re-plot the data so that each type of wood is plotted in a different colour. 
Save the plot as a .png file
'''


import csv 
from matplotlib import pyplot as plt
from math import pi

with open('beam_data.csv') as file:
    
    reader = csv.reader(file)
    
    # Remove header from data
    data = list(reader)[2:] 
    

    width, height, youngs, length, density = [], [], [], [], []
    
    # Store imported data 
    for d in data:

        youngs.append(float(d[4])*10**(9))   # Convert units from GPa -> Pa
        density.append(float(d[5]))   
        length.append(float(d[6])*0.01)      # Convert units from cm to m
        width.append(float(d[8])*0.01)       # Convert units from cm to m
        height.append(float(d[9])*0.01)      # Convert units from cm to m
        
    frequency = []
    
    # Data structure to store density and frequency of each type of wood for plotting 
    wood_a = [[],[]]
    wood_b = [[],[]]
    wood_c = [[],[]]
    wood_d = [[],[]]
        
    for w, h, E, L, rho in zip(width, height, youngs, length, density):
        
        # Compute second moment of area
        I = w * h**3 / 12
        
        # Compute the natural frequency
        f_n = pi/(2 * L**2) * ((E * I) / (rho * w * h))**(1/2)
        
        frequency.append(f_n)
        
        # Sort the beams into four groups, clustered by similar density values 
        if rho < 200:
            wood_a[0].append(rho)
            wood_a[1].append(f_n)
        elif 400 < rho < 600:
            wood_b[0].append(rho)
            wood_b[1].append(f_n)
        elif 600 < rho < 800:
            wood_c[0].append(rho)
            wood_c[1].append(f_n)
        else:
            wood_d[0].append(rho)
            wood_d[1].append(f_n)
            
    # Plot all data
    plt.plot(density, frequency, 'o')
    plt.xlabel('Density kg/m^3')
    plt.ylabel('Natural frequency Hz')
    plt.show()
    
    # Plot the data with density clusters shown in different colours
    plt.plot(wood_a[0], wood_a[1], 'o', label='wood a')
    plt.plot(wood_b[0], wood_b[1], 'o', label='wood b')
    plt.plot(wood_c[0], wood_c[1], 'o', label='wood c')
    plt.plot(wood_d[0], wood_d[1], 'o', label='wood d')
    plt.xlabel('Density kg/m^3')
    plt.ylabel('Natural frequency Hz')
    plt.legend()
    plt.savefig('wood.png')
    plt.show()
        