import cv2
import numpy as np

img = cv2.imread('opencv-logo2.png')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_LINEAR)

# Show blobs
cv2.imshow("original", img)
cv2.imshow("resized", res)
cv2.waitKey(0)