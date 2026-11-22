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

    # Return the most common label
    return max(votes, key=votes.get)


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
    for i in range(n):
        for j in range(0, n-i-1):
            if distances[j][0] > distances[j+1][0]:
                distances[j], distances[j+1] = distances[j+1], distances[j]

    # Count the labels of the k nearest neighbours
    votes = {}
    for i in range(k):
        label = distances[i][1]
        votes[label] = votes.get(label, 0) + 1

    # Return the most common label
    return max(votes, key=votes.get)

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

def measure_time(algorithm, data, new_observation):

    start_time = time.perf_counter()

    algorithm(data, new_observation)

    end_time = time.perf_counter()

    execution_time = end_time - start_time
    # print(f'Algorithm A took {execution_time} seconds' )

    return execution_time # seconds

def measure_space(algorithm, data, new_observation):

    tracemalloc.start()

    algorithm(data, new_observation)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    peak_memory_used = peak / 1024 # KB

    # print(f'Peak memory usage = {peak / 1024} KB')
    return peak_memory_used

# def main(args):
#     return

def main(args):

    with open('obstacle_avoidance_data.csv', newline='') as file:
        data = list(csv.reader(file))

    # Format data correctly for knn algorithm
    data_formatted = []

    # Exclude the headings from the data
    for line in data[1:]:
        line_formatted = ([float(line[0]), float(line[1]), float(line[2])], 
                        (line[3]))
        data_formatted.append(line_formatted)

    # Randomly generate some observations 
    new_observations = [generate_random_observation(data_formatted) for i in range(3)]

    all_results = []

    # Test different values of n
    # for n in [10000, 5000, 1000]:
    # for n in [1000, 500, 100]:
    for n in [5000, 1000, 500]:
        print(f'Testing {n} observations...')

        # Downsample data to correct size n
        data_formatted = data_formatted[:n]

        if '--knn_A' in args:
            algorithm = knn_A
            big_O_time = n
            big_O_space = 1

        else:
            algorithm = knn_B
            big_O_time = n**2
            big_O_space = n

        # Measure execution time  
        time_measured = [measure_time(algorithm, 
                                      data_formatted, 
                                      observation) 
                                      for observation in new_observations]
        
        time_measured_average = sum(time_measured)/len(time_measured)

        seconds_per_operation = time_measured_average/big_O_time
        # seconds_per_operation = big_O_time/time_measured_average

        # Measure peak memory usage
        space_measured = [measure_space(algorithm, 
                                        data_formatted, 
                                        observation) 
                                        for observation in new_observations]
        
        space_measured_average = sum(space_measured)/len(space_measured)

        KB_per_memory = space_measured_average/big_O_space

        # Save value of n to results
        # results = [n, big_O_time, average_time_measured, normalised_average_time_measured, 
        #            big_O_space, average_space_measured, normalised_average_space_measured]
        results = { 'n': n,
                    'operations': big_O_time,
                    'time (seconds)': time_measured_average,
                    'seconds/operation': seconds_per_operation,
                    'data': big_O_space,
                    'memory (KB)': space_measured_average,
                    'KB/data': KB_per_memory
                    }
        
        all_results.append(results)

    algorithm = 'knn_A' if '--knn_A' in args else 'knn_B'

    with open(f'output_data_{algorithm}.csv', 'w', newline = '') as file:
        
        writer = csv.writer(file)
        writer.writerow(all_results[0].keys())

        for result in all_results:
            writer.writerow(result.values())

    # Engineering suitability
    print()
    print(f"----------{algorithm}: configurations that meet engineering constraints---------------")

    # Configurations that meet engineering contraints with ...
    meets_constraints = {3 : [],        # 3 sensors
                         10: [],        # 10 sensors                                   
                         100: [],       # 100 sensors
                         1000: []       # 1000 sensors
                         }

    for result in all_results:
        for number_of_sensors in meets_constraints:

            # Estimate time to run algorithm at current number of sensors
            estimated_time = number_of_sensors * result['time (seconds)'] / 3

            # Store if engineering constraints are met 
            if estimated_time <= 0.01 and result['memory (KB)'] <= 32:
                meets_constraints[number_of_sensors].append(f"{result['n']} observations")

    for i,j in meets_constraints.items():
        print(f'Number of sensors: {i}, {j}' )



if __name__ == '__main__':
    
    #This line will run the main function of your code - uncomment this when you're ready to run everything.
	main(sys.argv[1:])
     
    #The code below will run the knn_A and knn_B functions to classify the example new observation
    #Delete/comment out these line and run the main function instead 
    # new_observation = generate_random_observation(sample_data)
    # print(knn_A(sample_data, new_observation, 3))
    # print(knn_B(sample_data, new_observation, 3))

    


    
