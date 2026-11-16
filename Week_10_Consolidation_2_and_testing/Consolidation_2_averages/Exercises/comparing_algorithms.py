import sys 
import time 
import csv
import tracemalloc
import glob


sample_data = [
    ([1, 2], "cat"),
    ([2, 3], "cat"),
    ([3, 3], "cat"),
    ([6, 7], "dog"),
    ([7, 8], "dog"),
    ([8, 7], "dog"),
    ([2, 6], "cat"),
    ([7, 3], "dog")
]

def knn_A(training_data, new_observation, k):
    """
    Sorts all the distances using bubble sort
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


def knn_B(training_data, new_observation, k):
    """
    Maintains a sorted list containing only the k closest observations
    """
    nearest = []

    # Calculate distance to every training observation
    for features, label in training_data:
        distance = 0
        for i in range(len(new_observation)):
            distance += (features[i] - new_observation[i])**2

        # Update sorted list to contain only the k closest observations
        # Find where this observation belongs
        position = 0
        while position < len(nearest) and nearest[position][0] < distance:
            position += 1

        # Insert into the sorted list
        nearest.insert(position, (distance, label))

        # Keep only the k nearest neighbours
        if len(nearest) > k:
            nearest.pop()

    # Count the labels of the k nearest neighbours
    votes = {}
    for distance, label in nearest:
        votes[label] = votes.get(label, 0) + 1

    # Return the most common label
    return max(votes, key=votes.get)

def calculate_mode(numbers):

    return 0.0

# def main(args):

#     return

def measure_time(algorithm, data, new_observation, k):

    start_time = time.perf_counter()

    algorithm(data, new_observation, k)

    end_time = time.perf_counter()

    execution_time = end_time - start_time
    # print(f'Algorithm A took {execution_time} seconds' )

    return execution_time # seconds

def measure_space(algorithm, data, new_observation, k):

    tracemalloc.start()

    algorithm(data, new_observation, k)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    peak_memory_used = peak / 1024 # KB

    # print(f'Peak memory usage = {peak / 1024} KB')
    return peak_memory_used

def main(args):

    for algorithm in [knn_A, knn_B]:

        algorithm_results = []

        if '--new_observation' in args:
            idx = args.index('--new_observation')
            new_observation = args[idx+1]
            new_observation = list(map(float, new_observation.split(',')))
        else:
            new_observation = [122, 130, 25]

        path = "knn_datasets"
        files = glob.glob(path + '/*.csv')
        files = [f for f in files if 'random' in f]

        for file in files:
            # Open each data file
            with open(file, newline='') as file:
                data = list(csv.reader(file))

            # Format data correctly for knn algorithm
            data_formatted = []
            for line in data[1:]:
                line_formatted = ([float(line[0]), float(line[1]), float(line[2])], 
                                (line[3]))
                data_formatted.append(line_formatted)

            # Compute number of observations in file
            n = len(data_formatted)

            # Aggregate
            results = [n]

            # Column headings for results file
            columns = ['n']

            # Test different value of k
            for k in [5,50,500]:

                columns.append('k='+str(k))

                # Compute big O complexity
                if '--measure_time' in args:
                    big_O = n**2 if algorithm==knn_A else n
                elif '--measure_space' in args:
                    big_O = n if algorithm==knn_A else k
                else:
                    big_O = None

                # Measure execution time or memory usage     
                if '--measure_time' in args:
                    measured_value = measure_time(algorithm, 
                                                  data_formatted, 
                                                  new_observation, 
                                                  k)

                elif '--measure_space' in args:
                    measured_value = measure_space(algorithm, 
                                                   data_formatted, 
                                                   new_observation, 
                                                   k)

                else:
                    measured_value = None
                    algorithm(data_formatted, new_observation, k)

                # Add the measured value at each k investigtaed 
                results.append(measured_value)

            # Aggregate the result for each value of n (number of observatons) investigated  
            algorithm_results.append(results)
        
        # Sort the results in orde rof n
        n_values = [i[0] for i in algorithm_results]
        algorithm_results = [result for _, result in sorted(zip(n_values, 
                                                                algorithm_results))]

        for result in algorithm_results:
            print(result)

        # Normalised results by dividing each measured value by big O
        normalised_results = algorithm_results.copy()

        for i, line in enumerate(normalised_results):
            normalised_results[i][1:] = [result/big_O if result!=None else None for result in line[1:]]

        for result in normalised_results:
            print(result)

        # Save the results
        if '--measure_time' in args:
            measured_value = 'time_(seconds)'
        elif '--measure_space' in args:
            measured_value = 'space_(KB)' 
        else:
            measured_value = '' 

        with open(f'output_data_{measured_value}.csv', 'w', newline = '') as file:
            writer = csv.writer(file)

            writer.writerow([f"Observation {new_observation}"]) 

            writer.writerow([f"{measured_value}"]) 
            # writer.writerow(['n', 'k=5', 'k=50', 'k=500'])    
            writer.writerow(columns)    
            writer.writerows(algorithm_results)

            writer.writerow([f"{measured_value} normalised to Big O"]) 
            writer.writerow(columns)    
            writer.writerows(normalised_results)

if __name__ == '__main__':
    
    #This line will run the main function of your code - uncomment this when you're ready to run everything.
	main(sys.argv[1:])
     
    #The code below will run the knn_A and knn_B functions to classify the example new observation
    #Delete/comment out these line and run the main function instead 
    # new_observation = [3, 4]
    # print(knn_A(sample_data, new_observation, 3))
    # print(knn_B(sample_data, new_observation, 3))