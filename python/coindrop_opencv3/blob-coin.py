#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("ourimg/image1tm.jpg", cv2.IMREAD_GRAYSCALE)

myver = (cv2.__version__).split('.')
print (myver)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200

# Filter by Area.
params.filterByArea = True
params.minArea = 50
params.maxArea = 100

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.80

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)
pointflag = len(keypoints)
print(pointflag)
if pointflag == 1 :
	print("there's a coin")
elif pointflag > 1 :
	print("a coin and something else")
else :
	print("nothing there")
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

