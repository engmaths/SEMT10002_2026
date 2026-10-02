'''
## Exercise 3 - Solving Kepler's equation

Write some code using a `for` loop to solve Kepler's equation using fixed point iteration with 100 steps.
Find the true anomaly $E$ for mean anomaly $M=1.54$ and eccentricity $e=0.3$.

> Hint: re-arrange Kepler's equation into the form $E = f(E)$

Add an early stopping criterion to end the iterations when Kepler's equation is satisfied to within $0.01\%$ of the mean anomaly $M$.

'''

# get access to the sin function
from math import sin

# set and print the known values
M = 1.54
e = 0.3
print('Mean anomaly M is',M)
print('Eccentricity e is',e)

# guess
E = M

# fixed point iteration
for ii in range(20):
    E = M+e*sin(E) # Kepler's equation re-arranged to E = f(E)
    print('Step',ii,'E=',E,'E-esinE=',E-e*sin(E),'M=',M,'Error=',E-e*sin(E)-M)
