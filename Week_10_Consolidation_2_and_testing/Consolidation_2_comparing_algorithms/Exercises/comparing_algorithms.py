import sys 
import csv
import time 
import tracemalloc
import random

# Random numbers generated will be the same each time the code runs 
random.seed(42)

sample_data = [
    ([100, 100, 100], "clear"),
    ([80, 90, 85],    "clear"),
    ([20, 100, 100],  "obstacle left"),
    ([15, 30, 100],   "obstacle left"),
    ([12, 34, 90],    "obstacle left"),
    ([90, 92, 95],    "clear"),
    ([112, 89, 102],  "clear"),
    ([17, 70, 95],    "obstacle left")
]

def knn_A(training_data, new_observation, k=5):

    """
    Maintains a sorted list containing only the k closest observations
    """

    nearest = []

    for features, label in training_data:

        # Step A: Calculate distance to every training observation
        distance = 0
        for i in range(len(new_observation)):
            distance += (features[i] - new_observation[i])**2

        # Step B: Maintains a sorted list containing only the k closest observations.
        # Add the new observation to the end of the list of closest observations
        nearest.append((distance, label))

        # Gets the index of the new observation in the list
        index = len(nearest) - 1

        # Work backwards through the list checking if each item is smaller than the item 
        # before it and swapping if it is, until all items have been checked
        while index > 0 and nearest[index-1][0] > nearest[index][0]:
            nearest[index], nearest[index-1] = nearest[index-1], nearest[index]
            index -= 1

        # Keep only the k nearest neighbours
        if len(nearest) > k:
            nearest.pop()

    # Step C: Count the labels of the k nearest neighbours
    votes = {}
    for distance, label in nearest:
        votes[label] = votes.get(label, 0) + 1

    # Find the most common label amongst the nearest neighbours
    # Initialise most common label as first in dictionary
    most_common_label = list(votes.keys())[0]

    # Return the most common label
    for label in votes:
        if votes[label] > votes[most_common_label]:
            most_common_label = label

    return most_common_label


def knn_B(training_data, new_observation, k=5):
    """
    Calculates the distance from the new observation to every training observation
    Sorts all the distances using bubble sort
    Counts the labels of the k nearest neighbours
    Returns the most common label
    """
    distances = []

    # Calculate distance to every training observation
    for features, label in training_data:
        distance = 0
        for i in range(len(new_observation)):
            distance += (features[i] - new_observation[i])**2
        distances.append((distance, label))

    # Sort all distances using bubble sort
    n = len(distances)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if distances[j][0] > distances[j+1][0]:
                distances[j], distances[j+1] = distances[j+1], distances[j]

    # Count the labels of the k nearest neighbours
    votes = {}
    for i in range(k):
        label = distances[i][1]
        votes[label] = votes.get(label, 0) + 1

    # Find the most common label amongst the nearest neighbours
    # Initialise most common label as first in dictionary
    most_common_label = list(votes.keys())[0]

    # Return the most common label
    for label in votes:
        if votes[label] > votes[most_common_label]:
            most_common_label = label

    return most_common_label
    

def generate_random_observation(training_data):
    all_values = []

    for observation, label in training_data:
        for value in observation:
            all_values.append(value)

    min_value = min(all_values)
    max_value = max(all_values)

    new_observation = [
        random.uniform(min_value, max_value),
        random.uniform(min_value, max_value),
        random.uniform(min_value, max_value)
    ]

    return new_observation


def main(args):
    return


if __name__ == '__main__':
    
    #This line will run the main function of your code - uncomment this when you're ready to run everything.
	# main(sys.argv[1:])
     
    #The code below will run the knn_A and knn_B functions to classify the example new observation
    #Delete/comment out these line and run the main function instead 
    new_observation = generate_random_observation(sample_data)
    print(new_observation)
    print(knn_A(sample_data, new_observation, 3))
    print(knn_B(sample_data, new_observation, 3))

    


    
