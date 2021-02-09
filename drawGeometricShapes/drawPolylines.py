import numpy as np
import cv2

# draw black canvas using numpy
img = np.zeros([512, 512, 3], np.uint8)

# array containing all the points
pts = np.array([[25, 70], [25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20]],
               np.int32)

pts = pts.reshape((-1, 1, 2))

# params:
# - image object
# - list of points
# - isClosed (is it a closed shape) if False, it leaves one edge open
# - color tuple
# - thickness
# - linetype

img = cv2.polylines(img, [pts], True, (000, 000, 255), 5, cv2.LINE_AA)

cv2.imshow('black', img)
cv2.waitKey(0)
