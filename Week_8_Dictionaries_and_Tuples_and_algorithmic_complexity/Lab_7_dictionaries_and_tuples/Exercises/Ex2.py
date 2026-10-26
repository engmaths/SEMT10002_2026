'''
================
Exercise 2
================

A dictionary is used to represent the weighted graph of the distances between cities via a major road network.<br>
The cities are represented as nodes, and the road connections as edges, labelled with the distance in km<br>
Write a program that does the following: 
a. Print the names of all cities with direct connections/edges to Dunvor
b. Add a new city, Glenby, that is 35 km from Fenwick, 5 km from Alden and 27 km from Brinford
c. The road is closed between Fenwick and Dunvor Remove this edge from the graph
d. Write and use a function that return the name of the city with the least direct connections to other cities
e. Write and use a function that returns the mean distance from one city to another across the whole network
}
'''


cities = {  "Alden":{    "Brinford":20, "Dunvor":8,     "Fenwick":12},
            "Brinford":{ "Alden":20,    "Caster":32,    "Dunvor":15},
            "Caster":{   "Brinford":32, "Dunvor":6,     "Fenwick":24},
            "Dunvor":{   "Alden":8,     "Brinford":15,  "Caster":6,     "Fenwick":10},
            "Elwick":{   "Caster":5,    "Fenwick":41},
            "Fenwick":{  "Alden":12,    "Dunvor":10,    "Caster":24,    "Elwick":41}
            }