KNN obstacle-avoidance datasets

Files
-----
Three random-order datasets cover all combinations:
  n = 1,000; 5,000; 20,000
 

Two additional files provide ordering comparisons for n=5,000:
  ascending_n5000.csv
  descending_n5000.csv

The corresponding random-order file is:
  random_n5000.csv

Columns
-------
left_cm, centre_cm, right_cm: three distance-sensor readings in centimetres
classification: Clear, Obstacle left, Obstacle ahead, or Obstacle right

For all experiments, use this fixed new observation:
  [50.0, 50.0, 50.0]

Ordering variants
-----------------
The ascending and descending files are ordered by Euclidean distance
from each row's three sensor readings to [50.0, 50.0, 50.0].
The random files contain the same type of observations in shuffled order.

