import numpy as np
import matplotlib.pyplot as plt

def perlin_terrain_gen(width):
    def perlin(x, y):
        return (np.sin(x * 0.1) + np.cos(y * 0.1)) * 5

    terrain = np.zeros((width, width))

    for i in range(width):
        for j in range(width):
            terrain[i, j] = perlin(i, j)

    return terrain

size = 100
Z = perlin_terrain_gen(size)

# Plot elevation map
plt.figure(figsize=(8, 6))
plt.imshow(Z, origin='lower', cmap='terrain')
plt.title("Elevation Map")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label="Elevation")
plt.show()
