import numpy as np
import cv2

# generate black image using numpy
# list of height, width, 3 or 4 (number of channels)
img = np.zeros([512, 512, 3], np.uint8)

cv2.imshow('black', img)
cv2.waitKey(0)
