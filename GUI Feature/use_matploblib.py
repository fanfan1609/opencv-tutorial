import numbers as np
import cv2
import os
from matplotlib import pylab as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'dog_1.jpg' )
img = cv2.imread(file_path, cv2.IMREAD_COLOR) 
img2 = img[:,:,::-1] # Switch color schema from BGR to RGB

# OpenCV follows BGR order, while Matplotlib follows RGB order
# below is the example for 2 way displays
# 1. Matplotlib
# f, ax = plt.subplots(2, sharey=True)
# ax[0].imshow(img) #expects distored color
# ax[1].imshow(img2) #expects true color
# plt.show()

# 2. OpenCV
cv2.imshow('BGR color',img) #expects true color
cv2.imshow('RGB color', img2) #expects distored color

cv2.waitKey(0)
cv2.destroyAllWindows()
