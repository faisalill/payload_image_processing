import cv2
import numpy as np
import matplotlib.pyplot as plt

def bilateral_filter(image):
#Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered_image = cv2.bilateralFilter(image_rgb, d=9, sigmaColor=75,
    sigmaSpace=75)

    return filtered_image
