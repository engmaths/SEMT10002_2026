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

# -------------------------------------------
# a
# -------------------------------------------
print("The cities with direct connections to Dunvor are", list(cities["Dunvor"].keys()))

# -------------------------------------------
# b
# -------------------------------------------
cities["Glenby"] = {"Alden": 5,
                    "Brinford":27,
                    "Fenwick":35
                    }

# -------------------------------------------
# c
# -------------------------------------------
cities["Dunvor"].pop("Fenwick")
cities["Fenwick"].pop("Dunvor")

# -------------------------------------------
# d
# -------------------------------------------
def least_connected(cities):
    """
    Return the name of the city with the least direct connections to other cities
    """

    least_connected = ""
    min_connections = 0

    for city, connections in cities.items():
        
        n_connections = len(connections)

        # Store number of connections of first city as current minimum
        if min_connections == 0 and n_connections >= 0:
            min_connections = n_connections

        # Compare every subsequent city to check for fewer connections
        elif n_connections < min_connections:
            min_connections = n_connections
            least_connected = city

    return least_connected

print("The city with the least connections is", least_connected(cities))
     
# -------------------------------------------
# e
# -------------------------------------------

def mean_distance(cities):
    total_distance = 0
    total_connections = 0
    explored = []
    for city_a, distances in cities.items():

        for city_b in distances:

            #Put in alphabetical order
            pair = sorted([city_a, city_b])

            # Check if the distance between the pair of cities has already been recorded
            if pair not in explored:
                explored.append(pair)
                total_distance += distances[city_b]
                total_connections += 1

    mean = total_distance / total_connections

    return mean

print("The mean distance from one city to another across the whole network =", mean_distance(cities), "km")