import cv2

# 1. READ AN IMAGE
# ways to read an image. 0 for grayscale, 1 for color, -1 for images with alpha channel.
# flag values for teh integers are cv2.IMREAD_GRAYSCALE, cv2.IMREAD_COLOR, cv2.IMREAD_UNCHANGED
img = cv2.imread('C:\\fakepath\\hackathon.png', 0)
# or cv2.imread('hackathon.png', cv2.IMREAD_GRAYSCALE)
print(img)

# TO display the image on a new window
# 1st field is a name for the new file and 2nd field is the image to display
cv2.imshow('readAndShow', img)

# no. of seconds the window should eb displayed for. 0 is default for window to stay open.
cv2.waitKey(0)

# closes all teh windows once the program is shut or the window is closed
cv2.destroyAllWindows()

# write an image with the image name and path as 1st arg and the img to write as second
ab = cv2.imwrite('C:\\fakepath\\readShowWrite.png', img)

# prints true if created
print(ab)

# ------------------------
