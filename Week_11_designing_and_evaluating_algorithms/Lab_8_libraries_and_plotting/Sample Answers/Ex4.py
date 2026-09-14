'''
================
Exercise 4
================


During the Covid-19 pandemic, a city recorded the number of infected individuals for one year. 
You are going to plot the raw data showing a time series of the number of infected individuals, and on the same axes 
plot a logistic growth curve to observe whether if fits the raw data.
Whereas exponential population growth shows rapid population growth if resources were not a factor.
Logistic population growth models population growth and the decrease of the growth as the population meets the 
carrying capacity or sustainable resource limit.


1. Import data about the city from 'city_info.csv'

2. Import time series data about number of infected individuals from 'infection_data.csv'

3. Use the data in 'infection_data.csv' to plot the raw data on the fraction of the population infected at each timesetp as a scatter plot. 

4. Plot the logistic growth curve $f(t)$ where $f$ is the fraction of the population that has been infected at time $t$, using parameters from 'city_info.csv', for all timesteps $t$ in 'infection_data.csv'

For both the logistic growth curve and the raw data, remember to normalise the data on number of infected individuals to be a fraction of the totoal population
'''
import csv
import matplotlib.pyplot as plt
from math import exp

# Import city info
with open('city_info.csv') as file:
    reader = csv.reader(file)
    city_data = list(reader)
    print(city_data)
    
# Create dictionary representation of city data
city_info = {}
for i in city_data:
    city_info[i[0]] = float(i[1])
print(city_info)

# Import infection data
with open('infection_data.csv') as file:
    reader = csv.reader(file)
    
    # Remove header
    infection_data = list(reader)[1:]
    
    time, infected = [], []
    
    for item in infection_data:
        time.append(int(item[0]))
        infected.append(int(item[1]))

# Normalise infected indicviduals to get values as fraction of the population infected  
infected_n = []
for i in infected:
    infected_n.append(i / city_info["Total population"])

# Plot raw data time series 
plt.plot(time, infected_n, 'o', label = "raw data")

# Generate logistic growth time series of fraction of the population infected 
N = city_info["Total population"]
r = city_info["Infection rate"]
f_0 = city_info["Initial number of infected individuals"] / N
f_inf = city_info["Final number of infected individuals"] / N
series = []

for t in time:
    series.append(f_0 * f_inf / (f_0 + (f_inf - f_0) * exp(-r * t)))

# Plot logistic growth time series
plt.plot(time, series, label = "logistic function")

# Add axes and data labels
plt.xlabel('Time (days)')
plt.ylabel('Fraction of population')
plt.legend()
plt.show()