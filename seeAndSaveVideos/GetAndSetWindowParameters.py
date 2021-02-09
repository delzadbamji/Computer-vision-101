import cv2

cap = cv2.VideoCapture(0)

# cap.set is for setting the window properties
# cv2.CAP_PROP_FRAME_WIDTH , cv2.CAP_PROP_FRAME_HEIGHT can be changed using set property
# frame_width and height flags can be replaced with integer values corresponding to the flags.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
# cap.set(3, 1208)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cap.set(4,720)

'''
NOTE: even though we can set the 2nd parameter to any random value, the frame dimensions will only take up the 
nearest available dimensions.
'''
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('readFrame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



# ----------------------2----------------------- GET PROPERTIES OF CAPTURE CLASS

# The width and height can be fetched using:
# cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# OTHER PROPERTIES THAT CAN BE FOUND ARE ON:
# https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

