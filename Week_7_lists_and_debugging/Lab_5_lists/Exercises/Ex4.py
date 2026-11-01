"""
================
Exercise 4
================


Paste the code below that you wrote for Consolidation Exercise 1, or the template you were given 
for Consolidation exercise 1 -- either is OK. 

a) Give the robot a sequence of points, your robot should move the robot to visit each point 
in sequence.The plotter library has also been updated to `robot_plotter_v2` (remember to 
import it at the start of your code) and the `show_plot` function now takes a data struture of 
mutiple x,y points allowing you to plot multiple goals. It's not essential that you use this, 
but it will allow you to plot multiple goals, instead of one, in the visualisation. 

b) Make our robot do a search pattern, known fancily as the boustrephedon or more colloquially 
as the lawnmower.
The robot should:<br>
    1. start at point (1000, 1000), facing in the **positive horizontal** direction <br>
    2. move 2000 units in the **positive horizontal** direction<br>
    3. move 8000 units in the **positive vertical** direction<br>
    4. move 2000 units in the **positive horizontal** direction<br>
    5. move 8000 units in the **negative vertical** direction<br>
    6. *repeat* steps 2-5 twice in total 
    7. stop
    
c) If you managed to get to the part about obstacle avoidance in Consolidation Exercise 1, test 
if your controller still works if there is an obstacle present 
"""