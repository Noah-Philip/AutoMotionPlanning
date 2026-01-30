import math as m
import terrain_generation as terraingen
from robot import Robot
import random as rand

#Sim parameters
map_size = 10
dt = 0.02 #Fixed timestep (50 Hz)
sim_time = 5.0 #num of seconds
numSteps = int(sim_time / dt)

#Starting Point
# startX = rand.randint(0, map_size - 1)
# startY = rand.randint(0, map_size - 1)
startX = 0
startY = 0

#Ending Point
# endX = rand.randint(0, map_size - 1)
# endY = rand.randint(0, map_size - 1)
endX = 9
endY = 9

#Map
cells = terraingen.perlin_terrain_gen(map_size)

robot = Robot(startX, startY)

