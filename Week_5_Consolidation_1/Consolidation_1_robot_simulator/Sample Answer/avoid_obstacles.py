from robot_plotter import init_plot, snapshot, show_plot
from math import sin, cos, atan2, sqrt
from random import random

# constants about the robot
robot_name = "Daneel"
robot_radius = 160
wheel_separation = 150
robot_wheel_radius = 35

# initial robot configuration
robot_x_position = 500
robot_y_position = 500
robot_heading = 0

#Map information
map_x_min = 0
map_x_max = 5000
map_y_min  = 0
map_y_max = 5000
map_coords = ((map_x_min, map_x_max), (map_y_min, map_y_max))
#This represents an obstacle at x = 100, y = 2250, with a width of 500 and a height of 800.
obstacle_x = 100
obstacle_y = 2250
obstacle_width = 4000
obstacle_height = 500
obstacle = ((obstacle_x, obstacle_y), (obstacle_width, obstacle_height))
goal = (1000, 4000)

#This is the number of timesteps we simulate- change as is necessary.
num_steps = 200
#This is the default timestep - so by default we'll simulate 100 timesteps of 1 second= 100 seconds of movement. 
delta_t= 1 

def sinc(angle_change):
    
    #Use Taylor series is angle change is small
    if angle_change**2<0.01**2:
        the_sinc = 1-(0.25*angle_change*angle_change/6.0)
    else:
        the_sinc = sin(0.5*angle_change)/(0.5*angle_change)

    return the_sinc


def update_pose(robot_x_position, robot_y_position, robot_heading, ang_speed_left, ang_speed_right, robot_wheel_radius, wheel_separation):

    '''
    Calculate new pose (x, y, heading) of robot given wheel speeds and robot parameters
    '''

    #Linear speed of each wheel is just angular speed x radius
    linear_speed_left = ang_speed_left * robot_wheel_radius
    linear_speed_right = ang_speed_right * robot_wheel_radius
    # angular speed of the robot is given by the difference in speeds divided by wheel spacing
    ang_speed_robot = (linear_speed_left - linear_speed_right) / wheel_separation
    # multiply angular speed by time to get the amount the angle has changed.
    angle_change = ang_speed_robot * delta_t

    ave_speed = 0.5*(linear_speed_left + linear_speed_right)

    # sinc
    the_sinc = sinc(angle_change)

    # update state
    robot_x_position = robot_x_position + ave_speed*delta_t*the_sinc*sin(robot_heading + 0.5*angle_change)
    robot_y_position = robot_y_position + ave_speed*delta_t*the_sinc*cos(robot_heading + 0.5*angle_change)
    robot_heading = robot_heading + angle_change

    return robot_x_position, robot_y_position, robot_heading


def get_distance_to_target(x, y, goal):

    #Euclidean distance between (x, y) and goal
     
    x_distance = goal[0] - x
    y_distance = goal[1] - y
    
    return sqrt(x_distance**2 + y_distance**2)


def get_angle_to_target(x, y, goal):

    #Use inverse tangent to get angle towards goal
     
    x_distance = goal[0] - x
    y_distance = goal[1] - y

    return atan2(x_distance, y_distance) 


def get_wheel_speeds(distance_to_target, heading_error):

    '''
    Determine appropriate wheel speeds based on current distance to target and heading error
    '''


    #If close to the goal, then stop
    if distance_to_target < 5:
        ang_speed_left = 0
        ang_speed_right = 0
        print("Stopped")
    #If heading error is large, then just turn on the spot
    elif heading_error > 0.01:
        #Use heading error as control signal- large error means fast turn, small error means slow turn.
        ang_speed_left = heading_error 
        ang_speed_right = -heading_error
        print("Turning")
    else:
        #If heading error is small and we're far from the goal, then mostly go forward, but use heading error for small corrections
        ang_speed_left = 1 + heading_error
        ang_speed_right = 1 - heading_error
        print("Moving straight")

    return (ang_speed_left, ang_speed_right)


def check_for_collisions(x_position, y_position, map_coords, obstacle):

    #Check for collision with map wall
    if x_position > map_coords[0][0] and x_position < map_coords[0][1] and y_position > map_coords[1][0] and y_position < map_coords[1][1]:
        #Check for collision with obstacle
        if x_position < obstacle[0][0] or x_position > obstacle[0][0] + obstacle[1][0] or y_position < obstacle[0][1] or y_position > obstacle[0][1] + obstacle[1][1]:
            return False
        else:
            return True 
    else:
        return True


def main(robot_x_position, robot_y_position, robot_heading, map_coords, obstacle):

    #Initalise plotting
    init_plot(robot_x_position,robot_y_position,robot_heading)

    #Set wheel speeds randomly
    ang_speed_left = 3.0 * random()
    ang_speed_right = 3.0 * random()

    #Main simulation loop
    for ii in range(num_steps):
            
        distance_to_target = get_distance_to_target(robot_x_position, robot_y_position, goal)
        angle_to_target = get_angle_to_target(robot_x_position, robot_y_position, goal)
        heading_error = angle_to_target - robot_heading
        print("Distance to target: ", distance_to_target)
        print("Angle to target: ", angle_to_target, ", Heading error: ", heading_error)

        #Get new positions, but don't overwrite old position yet- we need to check if the new position is collision free
        new_x_position, new_y_position, new_heading = update_pose(robot_x_position, robot_y_position, robot_heading, ang_speed_left, ang_speed_right, robot_wheel_radius, wheel_separation)

        #Check for collisions
        if not check_for_collisions(new_x_position, new_y_position, map_coords, obstacle):

            #No collision - we can safely update the state
            robot_x_position = new_x_position
            robot_y_position = new_y_position
            robot_heading = new_heading

            #Choose new random wheel speeds
            ang_speed_left = 3.0 * random()
            ang_speed_right = 3.0 * random()
        else:
            #Collision - set wheel speeds to rotate on the spot.
            ang_speed_left = -5
            ang_speed_right = 5   

        print("X position: ", robot_x_position, ", Y position:", robot_y_position, ", Heading: ", robot_heading)
        snapshot(robot_x_position,robot_y_position,robot_heading)

        show_plot(map_coords, goal=goal, obstacle=obstacle, pause=0.1)

    show_plot(map_coords, goal=goal, obstacle=obstacle)
    
if __name__ == "__main__":
    main(robot_x_position, robot_y_position, robot_heading, map_coords, obstacle) 
