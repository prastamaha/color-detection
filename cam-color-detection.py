import cv2
import numpy as np

video = cv2.VideoCapture(0)
print('''
Red     [r]
Blue    [b]
Green   [g]
Yellow  [y]
''')
color = input('what color do you want to detect? ')

print("press 'q' to exit program")

while True:
    _, frame = video.read()

    # convert bgr to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # detect red color
    redLower = np.array([170, 160, 25])
    redUpper = np.array([179, 255, 255])
    redMask = cv2.inRange(hsv, redLower, redUpper)
    redFrame = cv2.bitwise_and(frame, frame, mask=redMask)

    # detect Yellow
    yellowLower = np.array([20, 50, 20])
    yellowUpper = np.array([38, 255, 255])
    yellowMask = cv2.inRange(hsv, yellowLower, yellowUpper)
    yellowFrame = cv2.bitwise_and(frame, frame, mask=yellowMask)

    # detect Green
    greenLower = np.array([30, 52, 20])
    greenUpper = np.array([90, 255, 255])
    greenMask = cv2.inRange(hsv, greenLower, greenUpper)
    greenFrame = cv2.bitwise_and(frame, frame, mask=greenMask)

    # detect Blue
    blueLower = np.array([94, 80, 2])
    blueUpper = np.array([126, 255, 255])
    blueMask = cv2.inRange(hsv, blueLower, blueUpper)
    blueFrame = cv2.bitwise_and(frame, frame, mask=blueMask)

    
    if color == 'r':
        cv2.imshow('Normal x green', np.hstack([frame, redFrame]))
    elif color == 'b':
        cv2.imshow('Normal x green', np.hstack([frame, blueFrame]))
    elif color == 'g':
        cv2.imshow('Normal x green', np.hstack([frame, greenFrame]))
    elif color == 'y':
        cv2.imshow('Normal x green', np.hstack([frame, yellowFrame]))

    key = cv2.waitKey(1)
    if key == ord('q'):
        break