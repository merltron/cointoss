#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import glob
import datetime as dt

# Read image
# img = cv2.imread('camera-capture-hires-basic.jpg')
img = cv2.imread('capture_hb/cam17.jpg')


# hsv = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# th, thresh1 = cv2.threshold(gray, 200, 255, cv2.THRESH_TOZERO_INV)
# thresh = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY)

# ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#### OTHER ALGORHYTMS TO TRY 68,81,225

# HIGH LIGHT RANGE
dfactor=0.9
ifactor=1.5

mlo_b = 190
mlo_g = 189
mlo_r  = 223

lower = np.array([mlo_b*dfactor, mlo_g*dfactor, mlo_r*dfactor])
upper = np.array([mlo_b*ifactor, mlo_g*ifactor, mlo_r*ifactor])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(img, lower, upper)

thresh = cv2.bitwise_not(mask)
# thresh = gray

## Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

## Change thresholds
params.minThreshold = 100
params.maxThreshold = 200

## Filter by Area.
params.filterByArea = True
params.minArea = 180
params.maxArea = 800

## Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.80

## Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.89

## Filter by Color
filterByColor = False
# blobColor = 255

## Filter by Inertia
# params.filterByInertia = False
# params.minInertiaRatio = 0.2

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(thresh)
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

im_with_keypoints = cv2.drawKeypoints(thresh, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# timestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# font = cv2.FONT_HERSHEY_SIMPLEX
# final = cv2.putText(im_with_keypoints,timestamp,(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)


# Show blobs
cv2.namedWindow('Keypoints',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Keypoints', 1080,811)
cv2.imshow('Keypoints',im_with_keypoints)
cv2.imwrite("reflectoutput.jpg", im_with_keypoints)
cv2.waitKey(0)

