import cv2


# ---------------------draw line----------------
img = cv2.imread('C:\\fakepath\\hackathon.png', 1)

# param:
# - image object
# - tuple coordinates of p1 (start) x1,y1
# - tuple coordinates of p2 (end) x2,y2
# - color in bgr (b,g,r). Blue is (255,0,0)
#  - thickness (numbers)

img = cv2.line(img, (0, 0), (600, 255), (255, 0, 0), 5)

# for an arrowed line the function is :
img = cv2.arrowedLine(img, (0, 0), (550, 350), (255, 0, 0), 5)


cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
