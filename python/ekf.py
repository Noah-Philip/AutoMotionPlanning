import numpy as np

#Class used to estimate x, y, theta, velocity, bias,
#even though the robot doesnt see it directly!  
class EKF:
    def __init__(self, x0):
        self.x = x0 #state vector

        #Convariance Matrix -> Represents uncertainty (large values = uncertain)
        self.P = np.eye(5) * 0.1

        self.Q = np.diag([0.01, 0.01, 0.01, 0.1, 0.001])
        self.R = np.diag([0.05, 0.05])

    #Uses the motion model xk+1​=f(xk​,u)
    #Basically tells the program to say based on the current velocity and yaw, where should i be?
    #increase uncertainty as well
    def predict(self, u, dt):
        v, omega = u
        x, y, theta, velocity, b = self.x

        theta += (omega - b) * dt
        x += v * np.cos(theta) * dt
        y += v * np.sin(theta) * dt
        vel = v

        self.x = np.array([x, y, theta, velocity, b])

        F = np.eye(5)
        F[0, 2] = -v*np.sin(theta) * dt
        F[1, 2] = -v*np.cos(theta) * dt
        F[2, 4] = -dt

        self.P = F @ self.P @ F.T + self.Q
    def update(self, z):
        #Looks at position from terrain lookup (The fake GPS)
        H = np.zeros((2, 5))
        H[0, 0] = 1
        H[1, 1] = 1

        y = z - H @ self.x
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)

        self.x = self.x + K @ y
        self.P = (np.eye(5) - K @ H) @ self.P




