import numpy as np
import cv2
import matplotlib.pyplot as plt

class KalmanFilter(object):
    def __init__(self, F = None, B = None, H = None, Q = None, R = None, P = None, x0 = None):

        if(F is None or H is None):
            raise ValueError("Set proper system dynamics.")

        self.n = F.shape[1]
        self.m = H.shape[1]

        self.F = F
        self.H = H
        self.B = 0 if B is None else B
        self.Q = np.eye(self.n) if Q is None else Q
        self.R = np.eye(self.m) if R is None else R
        self.P = np.eye(self.n) if P is None else P
        self.x = np.zeros((self.n, 1)) if x0 is None else x0

    def predict(self, u = 0):
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        return self.x

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        S = self.R + np.dot(self.H, np.dot(self.P, self.H.T))
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.n)
        self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P),
        	(I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R), K.T)

def kalman_filter(img):
    print("Kalam Filter Triggered")
    # Flatten the image to 1D array
    measurements = img.flatten()

    # Define system dynamics for the Kalman filter
    F = np.array([[1, 1], [0, 1]])  # State transition matrix
    H = np.array([[1, 0]])          # Measurement matrix
    Q = np.array([[0.05, 0], [0, 0.05]])  # Process noise covariance
    R = np.array([[0.5]])                 # Measurement noise covariance

    # Initialize Kalman Filter
    kf = KalmanFilter(F = F, H = H, Q = Q, R = R)

    predictions = []

    # Apply Kalman filter to each pixel value
    for z in measurements:
        prediction = kf.predict()
        predictions.append(prediction[0])
        kf.update(z)

    # Convert the predictions back to the image shape
    filtered_img = np.array(predictions).reshape(img.shape)
    return filtered_img

