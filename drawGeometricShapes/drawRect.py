import cv2


# ---------------------draw Rect----------------
img = cv2.imread('C:\\Users\\Delzad\\PycharmProjects\\openCvTutorials\\hackathon.png', 1)


# params:
# - image obj
# - tuple top left vertex (x1,y1)
# - tuple bottom right vertex (x2,y2)
# - tuple color in bgr (b,g,r)
# - thickness  in int (-1 will fill the rect)

# x1,y1 ***********
#       *         *
#       *         *
#       *         *
#       *********** x2,y2

img = cv2.rectangle(img, (384, 0), (510, 128), (255, 0, 0), -1)
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()