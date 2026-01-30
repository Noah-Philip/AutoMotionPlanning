import simVariables as sim
import mazeSolver as ms
import math as m
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

start = (sim.startX, sim.startY)
end = (sim.endX, sim.endY)

rows, cols = sim.cells.shape
X, Y = np.meshgrid(range(cols), range(rows))
Z = sim.cells

path = ms.mazeSolve(sim.cells, start, end, sim.robot.step_size)
if path is None:
    print("no valid path!")
    exit()

path_index = 0
plt.close('all')
# 1. Set up the figure, axis, and initial plot element (the dot)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
mappable = cm.ScalarMappable(cmap='terrain')
mappable.set_array(Z)
ax.set_title("Elevation Map")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_aspect('equal')
fig.colorbar(mappable, ax=ax, label="Elevation")

ax.view_init(elev=45, azim=-60)
ax.set_zlabel("Elevation")


#plot the terrain surface
ax.plot_surface(
    X, Y, Z,
    cmap='terrain',
    linewidth=0,
    antialiased=True,
    alpha=0.9
)


#Plots the path on the terrain
path_x = [p[0] for p in path]
path_y = [p[1] for p in path]
path_z = [sim.cells[int(p[1]), int(p[0])]  for p in path] #changed

ax.plot(path_x, path_y, path_z, color='red', linewidth=2)

#Plots the actual robot, uses 3D scatter marker
robot, = ax.plot(
    [path_x[0]],
    [path_y[0]],
    [path_z[0]],
    marker='^',
    color='red',
    markersize=8
)


#Create a path line object to animate as the robot finds a path
path_line, = ax.plot([], [], [], color='red', linewidth=6)

# 2. Initialization function (optional, but good practice for a clean start)
def init():
    """Initializes the background of each frame."""
    path_line.set_data([], [])
    path_line.set_3d_properties([])
    return (path_line,)

# 3. Animation function: This is called sequentially for each frame
def animate(i):
    """Updates the position of the dot for frame i."""
    x, y = path[i]

    dx = path[min(i+1, len(path)-1)][0] - x
    dy = path[min(i+1, len(path)-1)][1] - y
    yaw = np.degrees(np.arctan2(dy, dx))

    robot.set_marker((3, 0, yaw))

    z = sim.cells[int(y), int(x)]  #changed

    #Animates the robot
    robot.set_data([x], [y])
    robot.set_3d_properties([z])

    path_x = [p[0] for p in path[:i+1]]
    path_y = [p[1] for p in path[:i+1]]
    path_z = [sim.cells[int(p[1]), int(p[0])]  for p in path[:i+1]]  #changed

    path_line.set_data(path_x, path_y)
    path_line.set_3d_properties(path_z)

    return (path_line)

# 4. Create the animation object
ani = animation.FuncAnimation(
    fig=fig,
    func=animate,
    init_func=init,
    frames=len(path), # Number of frames based on the path length
    interval=16, # Time delay between frames in milliseconds
    blit=False, # Optimizes drawing by only updating changed parts
    repeat=False # Animation runs only once
)

end_x, end_y = end

# Flag Pole to show the end point
end_z = sim.cells[int(end_y), int(end_x)] + 0.5
ax.plot([end_x, end_x], [end_y - 0.5, end_y + 0.8],
        color='black', linewidth=10)


# Flag Triangle (connects with the pole to create a flag)
ax.plot(end_x, end_y + 0.6,
        marker='>',
        color='red',
        markersize=40)


# To display the animation in a window
plt.show()
