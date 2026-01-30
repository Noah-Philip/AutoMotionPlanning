import random
import numpy as np
import matplotlib.pyplot as plt


def perlin_terrain_gen(width):
    # make a 10x10 maze-like structure
    maze = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
             [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [1, 1, 1, 0, 1, 1, 1, 1, 1, 0]]
    maze = np.array(maze) / 10.0
    # def perlin(X, Y):
    #     return maze[X, Y]

    # terrain = np.zeros((width, width))

    # for i in range(width):
    #     for j in range(width):
    #         terrain[i, j] = perlin(i, j)

    return np.array(maze)