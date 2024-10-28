import cv2
import numpy as np
import matplotlib.pyplot as plt

def average_box_filter(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    kernel_size = (5, 5)
    filtered_image = cv2.blur(image, kernel_size)
    return filtered_image
