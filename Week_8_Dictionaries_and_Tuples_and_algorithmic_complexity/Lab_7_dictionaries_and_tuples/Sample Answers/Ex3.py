'''
================
Exercise 3
================ 

Planet  Diameter (km)   Mass (relative to Earth = 1.00)   Rotation period 
Mercury 4,878           0.06                              58.65 (d) 
Venus   12,100          0.82                              243 (d)  
Earth   12,756          1.00                              23.934 (h)  
Mars    6,794           0.11                              24.623 (h)  
Jupiter 142,800         317.89                            9.842  (h)  
Saturn  120,000         95.17                             10.233 (h)  
Uranus  52,400          14.56                             16 (h) 
Neptune 48,400          17.24                             18 (h)   

1. Write a program that identifies and prints the name of the planet with the lowest density.
  Assume each planet is a perfect sphere

2. Write a program that identifies and prints the names and rotation periods of planets
 with a rotation period shorter than Earth's.
'''

from math import pi

planets = {
    "Mercury": {"diameter": 4878,  "mass": 0.06,    "rotation": 58.65,  "unit": "d"},
    "Venus":   {"diameter": 12100, "mass": 0.82,    "rotation": 243,    "unit": "d"},
    "Earth":   {"diameter": 12756, "mass": 1.00,    "rotation": 23.934, "unit": "h"},
    "Mars":    {"diameter": 6794,  "mass": 0.11,    "rotation": 24.623, "unit": "h"},
    "Jupiter": {"diameter": 142800, "mass": 317.89, "rotation": 9.842,  "unit": "h"},
    "Saturn":  {"diameter": 120000, "mass": 95.17,  "rotation": 10.233, "unit": "h"},
    "Uranus":  {"diameter": 52400,  "mass": 14.56,  "rotation": 16,     "unit": "h"},
    "Neptune": {"diameter": 48400,  "mass": 17.24,  "rotation": 18,     "unit": "h"}
}


# Identify and prints the name of the planet with the lowest density
min_density = None
name = None

for planet in planets:
    diameter = planets[planet]["diameter"]
    mass = planets[planet]["mass"]

    # Compute density 
    density = mass / (4/3 * pi * (diameter/2)**3)

    # If a new minimum is identified, store the density and planet name
    if min_density == None or density < min_density:
        min_density = density
        name = planet
  
print('The planet with the lowest density is', name)


"""
Identify and print the names and rotation periods of planets
with a rotation period shorter than Earth's
"""
earth_rotation = planets["Earth"]["rotation"]

for planet in planets:
    # Convert rotation periods measured in days to hours
    if planets[planet]["unit"] == "d":
        rotation = planets[planet]["rotation"] * earth_rotation
    else:
        rotation = planets[planet]["rotation"] 

    if rotation < earth_rotation:
        print(planet)