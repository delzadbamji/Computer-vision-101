import cv2


# ---------------------draw circle----------------
img = cv2.imread('C:\\Users\\Delzad\\PycharmProjects\\openCvTutorials\\hackathon.png', 1)


# params:
# - image obj
# - tuple center vertex (x1,y1)
# - radius in int
# - tuple color in bgr (b,g,r)
# - thickness  in int (-1 will fill the rect)

img = cv2.circle(img, (500, 366), 63, (255, 0, 0), -1)
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()