import time
import math as m

#Sim parameters

dt = 0.02 #Fixed timestep (50 Hz)
sim_time = 5.0 #num of seconds
numSteps = int(dt * sim_time)


#Robot States
x = 0.0
y = 0.0
yaw = 0.0
velocity = 0.0 #m/s

#Control Inputs
linearVelo = 1.0 # m/sec
yawRate = 0.3 # rads/sec

def simulationLoop():

    global x, y, yaw, velocity

    #Updates the robot states
    for i in range(numSteps):

        x += velocity * m.cos(yaw) * dt
        y += velocity * m.sin(yaw) * dt
        yaw += yawRate * dt
        velocity = linearVelo
    

def stuff(cells, startX, startY, endX, endY, rows, cols):
    #TODO
    pass

def inRange(cells, row, col):
    if row < 0 or row >= len(cells) or col < 0 or col >= len(cells[0]):
        return False
    return True


def mazeSolve(cells, start, end):
    return mazeSolveRecursively(cells, start, end)



def mazeSolveRecursively(cells, row, col, visited=None):
    if visited is None:
        visited = set()

    if not inRange(cells, row, col) or (row, col) in visited:
        return False

    if cells[row][col] == '$':
        return True
    
    visited.add((row, col))

    # Check all directions; if any return True, propagate it up
    if (mazeSolveRecursively(cells, row + 1, col, visited) or
        mazeSolveRecursively(cells, row - 1, col, visited) or
        mazeSolveRecursively(cells, row, col + 1, visited) or
        mazeSolveRecursively(cells, row, col - 1, visited)):
        return True

    return False
    
    



    


    
