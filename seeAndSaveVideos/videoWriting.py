import cv2

# ----------------------1----------------------- SAVE CAPTURED VIDEO

cap = cv2.VideoCapture(0)

# can be written as fourcc = cv2.VideoWriter_fourcc('X','V','I','D') also
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# video writer takes arguements:
# - name of output file,
# - fourcc code/ 4 byte code to specify video codec,
# - no. frames per sec,
# - size of output frame in a tuple
out = cv2.VideoWriter('C:\\fakepath\\out.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    # if ret ==True (file name/device code is correct) then save else break loop
    if ret:
        out.write(frame)
        cv2.imshow('writeFrame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
