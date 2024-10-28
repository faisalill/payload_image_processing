import cv2

def scharr_filter(image):

    print("Scharr Filter Triggered")

    scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0) # Gradient in the X
    scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)
    scharr_x = cv2.convertScaleAbs(scharr_x)
    scharr_y = cv2.convertScaleAbs(scharr_y)
    scharr_combined = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

    return scharr_combined

    
