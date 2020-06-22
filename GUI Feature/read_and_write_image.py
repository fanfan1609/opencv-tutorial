import os
import numpy as np
import cv2
import pathlib as Path
ESC_KEY = 27

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'dog_1.jpg' )

# Read image with cv2.imread
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE) # Load image with gray mode
cv2.imshow('image', img)

key = cv2.waitKey(0)
if key == ESC_KEY: # Wait for esc key to exit
    cv2.destroyAllWindows()
elif key == ord('s'): #wait for 's' key to save and exit
    cv2.imwrite(os.path.join(dir_path, 'dog_1_gray.png' ), img) # use fullpath for sure saving successfully
    cv2.destroyAllWindows()

