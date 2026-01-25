import math as m

class Robot:
    def __init__(self, x, y, step_size = 0.2):

        #Robot States
        self.x = float(x)
        self.y = float(y)
        self.z = 0.0
        self.yaw = 0.0
        self.velocity = 0.0

        self.step_size = step_size

        self.linear_velo = 1.0
        self.yaw_rate = 0.3

    def step(self, dt, terrain):
        self.x += self.velocity * m.cos(self.yaw) * dt
        self.y += self.velocity * m.sin(self.yaw) * dt
        self.yaw += self.yaw_rate * dt
        self.velocity = self.linear_vel

        ix, iy = int(self.x), int(self.y)
        if 0 <= ix < len(terrain) and 0 <= iy < len(terrain[0]):
            self.z = terrain[ix][iy]
        