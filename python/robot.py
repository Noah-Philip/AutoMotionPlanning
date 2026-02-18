import math as m
import numpy as np

class Robot:
    def __init__(self, x, y, step_size = .01):

        #Robot States
        self.x = float(x)
        self.y = float(y)
        self.z = 0.0
        self.yaw = 0.0
        self.velocity = 0.0

        #Sensor Noise + Bias
        self.encoder_std = 0.02
        self.gyro_std = 0.01
        self.accel_std = 0.05 

        self.gyro_bias = 0.05 #CONSTANT!    

        self.step_size = step_size

        self.linear_velo = 1.0
        self.yaw_rate = 0.3

    def step(self, dt, terrain):

        self.x += self.velocity * m.cos(self.yaw) * dt
        self.y += self.velocity * m.sin(self.yaw) * dt
        self.velocity = self.linear_velo
        ix, iy = int(self.x), int(self.y)
        if 0 <= ix < len(terrain) and 0 <= iy < len(terrain[0]):
            self.z = terrain[ix][iy]
    
    #Sensor simulations
    def read_encoders(self):
        noisy_v = self.velocity + np.random.normal(0, self.encoder_std)
        return noisy_v
    def read_imu(self):
        noisy_yaw_rate = self.yaw_rate + self.gyro_bias + np.random.normal(0, self.gyro_std)
        noisy_accel = np.random.normal(0, self.accel_std)
        return noisy_yaw_rate, noisy_accel