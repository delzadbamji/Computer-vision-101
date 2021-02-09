import cv2

# ----------------------1----------------------- CAPTURE VIDEO FROM FILE

# cap = cv2.VideoCapture(mp4 or some video file)

# ----------------------2----------------------- VIDEO CAPTURE CLASS FOR WEBCAM AND OTHER DEVICES

# for webcam, videocapture takes 0 or -1 as the argument.
# if you have other external cameras attached to the system, you can access them with 1 or 2 or 3...

# cap = cv2.VideoCapture(0)
#
# print(cap) prints and object

# ----------------------3----------------------- DISPLAY VIDEO AND CLOSE WITH KEYS

# # to continuously trap a video display we can add a while loop
# # ret returns true if it works and frame stores the captured video
#
# cap = cv2.VideoCapture(0)
#
# # isOpenened checks if the cap variable has legitimate data (file path or device index is correct)
# # and only then it will return true
# # alternately, we can use True in the while condition for it to always work
# while cap.isOpened():
#     ret, frame = cap.read()
#
# # shows the window with the name assigned in param0 and takes the frame in param1
#     cv2.imshow('readFrame', frame)
#
#     # closes the window if q key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


# ----------------------4----------------------- DIFFERENT COLOR CHANNELS

# to continuously trap a video display we can add a while loop
# ret returns true if it works and frame stores the captured video

cap = cv2.VideoCapture(0)

# isOpenened checks if the cap variable has legitimate data (file path or device index is correct)
# and only then it will return true
# alternately, we can use True in the while condition for it to always work
while cap.isOpened():
    ret, frame = cap.read()

#     to display the video in a different color channel than default(BGR)
#     here, gray

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# shows the window with the name assigned in param0 and takes the frame in param1
    cv2.imshow('readFrame', gray)

    # closes the window if q key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

