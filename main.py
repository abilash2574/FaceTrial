import face_recognition
import numpy as np
import cv2

# imgOriginal = face_recognition.load_image_file()
# imgOriginal = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2RGB)

"""
 In this we will learn how to work with openCV, the basic and other functions related to this project.
"""

img = cv2.imread("images/Gary-vee.png", 1)  # This is used for reading a image from a directory.

cv2.imshow('images', img)  # This is used to output the image.
cv2.waitKey(0)  # This is used so that the image is displayed until a keystroke is pressed.
cv2.destroyAllWindows()  # This destroys all the windows that are opened.

cam = cv2.VideoCapture(0)  # This is used to capture the video

while (cam.isOpened()):

    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('From video', gray)
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('my_image.png', frame)
        print('save')
    elif cv2.waitKey(1) == ord('q'):
        print('quit')
        break

cam.release()
cv2.destroyAllWindows()
