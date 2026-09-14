'''
================
Exercise 1
================

1. Create three lists of integers:

    x = [0,2,4,5,8,10,13]
    y = [1,3,3,3,4,5,6]
    z = [-3,0,1,0,4,6,7]

2. Generate a scatter plot of `y` against  `x`

3. On the same axes, create a line plot of `z` against `x`

4. Alter your figure so it has the following:
    - The line for `z` against `x` is red 
    - x axis label: `x`
    - A legend showing which data is `z` and which is `y`

5. Save your plot as a .pdf file
'''

import matplotlib.pyplot as plt

x = [0,2,4,5,8,10,13]
y = [1,3,3,3,4,5,6]
z = [-3,0,1,0,4,6,7]

plt.plot(x, y, 'o', label='y data')
plt.plot(x, z, 'r', label='z data')
plt.xlabel('x')
plt.savefig('figure_1.pdf')
plt.show()