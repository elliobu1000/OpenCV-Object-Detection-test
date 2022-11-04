
import cv2
import numpy as np
#import utlis










#Since we are creating a module and we want to run it as a standalone script as well
#we will add the if statement to check the file name. If this is the main module that was run then we will
#grab frame from our video and call the main function. In this case we will call the main function ‘getLaneCurve’
#since that is what we are interested in.



if __name__ == '__main__':
    cap = cv2.VideoCapture('vid.mp4')
    while True:
        success, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        cv2.imshow('Vid', img)

        cv2.waitKey(1)

