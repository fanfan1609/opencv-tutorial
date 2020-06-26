import os
import numpy as np
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'video.mp4' )

# Read video capture from file
cap = cv2.VideoCapture(file_path)

while(cap.isOpened()):
    # Read frame from video
    ret, frame = cap.read()
    
    # Convert frame color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # play video by showing frame
    cv2.imshow('frame', gray)

    # waitkey for break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close video resource
cap.release()

# close all windows
cv2.destroyAllWindows()
