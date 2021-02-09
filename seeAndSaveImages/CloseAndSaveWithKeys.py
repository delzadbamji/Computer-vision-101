import cv2

img = cv2.imread('C:\\fakepath\\hackathon.png', 0)
cv2.imshow('readAndShow', img)

# To trap the keys pressed :
# for 64 bit machines, it is preferred to use the mask(0xFF) to trap the key press
k = cv2.waitKey(0) & 0xFF

# we can check for the type of key pressed by using it's keycode. here, escape key:
if k == 27:
    cv2.destroyAllWindows()
# if it's a certain alphanum key, we can trap it as an ordinal
elif k == ord('s'):
    cv2.imwrite('C:\\fakepath\\readShowWrite.png', img)
    cv2.destroyAllWindows()
