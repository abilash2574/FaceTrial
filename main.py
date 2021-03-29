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

while True:  # We create a infinite loop that lets us show each frames that are captured from the camera

    ret, frame = cam.read()  # We Read the camera

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # We use this to change the BGR to Gray

    cv2.imshow('From video', frame)     # This is used to show the image in the window
    if cv2.waitKey(1) == ord('q'):  # use this to quit the loop: ord() is a function that let us match the character
        break
cam.release()
cv2.destroyAllWindows()
