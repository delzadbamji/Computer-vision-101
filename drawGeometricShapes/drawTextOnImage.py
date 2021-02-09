import cv2


# ---------------------text on image----------------
img = cv2.imread('C:\\fakepath\\hackathon.png', 1)


# params:
# - image obj
# - text to put
# - tuple starting point of text (x2,y2)
# - font face variable
# - font size
# - tuple color in bgr (b,g,r)
# - thickness  in int (-1 will fill the rect)
# - line type

font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.putText(img, 'pikachu',  (510, 128), font, 4, (255, 0, 0), 10, cv2.LINE_AA)
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
