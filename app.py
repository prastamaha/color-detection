import numpy as np 
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# batas warna
# define the list of boundaries 

boundaries = [
	([161, 155, 20], [179, 255, 255]),      # red
    ([94, 80, 20], [126, 255, 255]),        # blue
    ([35, 52, 20],[85,255,255]),            # green

]

for (lower, upper) in boundaries:
    lower = np.array(lower)
    upper = np.array(upper)

    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)  

