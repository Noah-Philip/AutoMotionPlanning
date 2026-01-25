import time
import math as m
import terrain_generation as terraingen
from robot import Robot
import random as rand

#Sim parameters
map_size = 100
dt = 0.02 #Fixed timestep (50 Hz)
sim_time = 5.0 #num of seconds
numSteps = int(dt * sim_time)

#Starting Point
startX = rand.randint(0, map_size - 1)
startY = rand.randint(0, map_size - 1)

#Ending Point
endX = rand.randint(0, map_size - 1)
endY = rand.randint(0, map_size - 1)

#Map
cells = terraingen.perlin_terrain_gen(map_size)

robot = Robot(startX, startY)

