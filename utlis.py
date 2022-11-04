


import cv2
import numpy as np





def thresholding(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([90, 0, 0])
    upperWhite = np.array([125, 255, 230])
    maskedWhite= cv2.inRange(hsv,lowerWhite,upperWhite)
    return maskedWhite