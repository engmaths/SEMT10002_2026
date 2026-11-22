comparing_algorithms.py contains two implementations of the k-NN aglorithm 

____________________________________________________________________________
Part 1 
____________________________________________________________________________
k-NN A has:
Time complexity O(nm)
Space complexity O(1)

k-NN B has:
Time complexity O(n^2) + O(nm)
Space complexity O(n)

____________________________________________________________________________
Part 2
____________________________________________________________________________

k-NN A
The time complexity varies approximately linearly with n as shown by the near-constant values in the column: seconds/operation
The space complexity is constant as shown by the constant value in the column: memory (KB), for all values of near
This valudates the predicted Big O complexity (above)

k-NN B
The time complexity varies approximately linearly with n^2 as shown by the near-constant values in the column: seconds/operation
The space complexity varies approximately linearly with n as shown by the same order of magnitude values in column: KB/data
This valudates the predicted Big O complexity (above)

____________________________________________________________________________
Part 3
____________________________________________________________________________

knn_A: configurations that meet the engineering constraints:
Number of sensors: 3, ['5000 observations', '1000 observations', '500 observations']
Number of sensors: 10, ['5000 observations', '1000 observations', '500 observations']
Number of sensors: 100, ['500 observations']
Number of sensors: 1000, []

knn_B: configurations that meet the engineering constraints:
Number of sensors: 3, ['500 observations']
Number of sensors: 10, []
Number of sensors: 100, []
Number of sensors: 1000, []