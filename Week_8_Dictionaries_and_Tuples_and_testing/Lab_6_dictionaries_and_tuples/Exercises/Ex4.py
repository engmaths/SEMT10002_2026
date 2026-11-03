'''
================
Exercise 4
================

Paste the code below that you wrote for Lab 5 - Lists, Exercise 4, or the template you were given 
for Consolidation exercise 1 -- either is OK. 

If you used a model of the roobt's state to build your robot controller, then you have already 
implemented a Finite State Machine model!
Can you implement this using a dictionary? 

If you didn't use state in your controller, you can expand on the FSM of a hypothetical robot given 
below instead. Draw out the FSM on a piece of paper. Can you add some new states and events that 
trigger them? How should you represent this in the dictionary? How can you test that the FSM model 
is working as expected?

'''

robot = {
    "GO_TO_GOAL": "REVERSE",
    "REVERSE": "TURN",
    "TURN": "MOVE_FORWARD",
    "MOVE_FORWARD": "GO_TO_GOAL",
}

def state_transition(robot, current_state):
    """
    Return the state of the robot after transitioning 
    """
    return(robot[current_state])

state = "GO_TO_GOAL"
state = state_transition(robot, state)
print(state)  # AVOIDING_OBSTACLE