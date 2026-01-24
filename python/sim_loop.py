import time
import math as m
import terrain_generation as terraingen
import random as rand

#Sim parameters
map_size = 100
dt = 0.02 #Fixed timestep (50 Hz)
sim_time = 5.0 #num of seconds
numSteps = int(dt * sim_time)

startX = rand.randint(0, map_size - 1)
startY = rand.randint(0, map_size - 1)

endX = rand.randint(0, map_size - 1)
endY = rand.randint(0, map_size - 1)

#Robot States
x = float(startX)
y = float(startY)
z = 0.0
yaw = 0.0
stepSize = 0.2 #Max possible z increase the robot can do in 1 iteration
velocity = 0.0

#Control Inputs
linearVelo = 1.0 # m/sec
yawRate = 0.3 # rads/sec

#Map
cells = terraingen.perlin_terrain_gen(map_size)

def simulationLoop():
    global x, y, z, yaw, velocity

    #Updates the robot states
    for _ in range(numSteps):

        x += velocity * m.cos(yaw) * dt
        y += velocity * m.sin(yaw) * dt
        z = cells[m.floor(x)][m.floor(y)]
        yaw += yawRate * dt
        velocity = linearVelo

        ix, iy = int(x), int(y)

        if inRange(cells, ix, iy):
            z = cells[ix][iy]

def stuff(cells, rows, cols):
    #TODO
    pass

def mazeSolve(cells, start, end):
    return mazeSolveRecursive(cells, start[0], start[1], cells[start[0]][start[1]], end)

def mazeSolveRecursive(cells, row, col, lastZ, end, visited=None):

    if not inRange(cells, row, col):
        return False

    currZ = cells[row][col]
    if(abs(lastZ - currZ) > stepSize):
        return False

    if visited is None:
        visited = set()

    if (row, col) in visited:
        return False

    if cells[row][col] == end:
        return True
    
    visited.add((row, col))
    if (mazeSolveRecursive(cells, row + 1, col, currZ, visited) or
        mazeSolveRecursive(cells, row - 1, col, currZ, visited) or
        mazeSolveRecursive(cells, row, col + 1, currZ, visited) or
        mazeSolveRecursive(cells, row, col - 1, currZ, visited)):
        return True
    return False

def inRange(cells, row, col):
    if row < 0 or row >= len(cells) or col < 0 or col >= len(cells[0]):
        return False
    return True