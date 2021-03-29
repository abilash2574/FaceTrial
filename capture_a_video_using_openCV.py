import cv2
import numpy as np


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # X264 is used for short videos and XVID for normal codec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)

        # Write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) ==  ord('q'):
            break
    else:
        break

# Release everything if job is finished

cap.release()
out.release()
cv2.destroyAllWindows()
