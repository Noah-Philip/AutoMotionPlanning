import numpy as np

def perlin_terrain_gen():
    def perlin(x, y):
        return (np.sin(x * 0.1) + np.cos(y * 0.1)) * 5

    size = 100
    terrain = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            terrain[i][j] = perlin(i, j)

    return terrain

def detailed_terrain_gen():
    #multiple layers of noise, rivers that flow downhill, natural procedural features
    pass


if __name__ == "__main__":
    terrain = perlin_terrain_gen()
    print(terrain)