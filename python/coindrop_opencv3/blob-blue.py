import cv2
import numpy as np
# cap = cv2.VideoCapture(0)

# Take each frame
frame = cv2.imread('capture_hb/cam3.jpg')

# Convert BGR to HSV
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# define range of blue color in HSV
# lower_blue = np.array([174,62,176])
# upper_blue = np.array([20,3,235])

# define range of blue color in HSV
lower_blue = np.array([140, 130, 170])
upper_blue = np.array([216, 205, 255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(frame, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)
# cv2.imshow('frame',frame)
cv2.imshow('res',res)
cv2.imwrite('grshit.png', res)
cv2.waitKey(0)
# k = cv2.waitKey(5) & 0xFF
# cv2.destroyAllWindows()