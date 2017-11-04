#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import glob
import datetime as dt

# Read image
# img = cv2.imread('camera-capture-hires-basic.jpg')
img = cv2.imread('capture_hb/cam7.jpg')
(x1, y1) = img.shape[:2]
target = img[:,:,[1,2,0]]

hsv = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# th, thresh1 = cv2.threshold(gray, 200, 255, cv2.THRESH_TOZERO_INV)
# thresh = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY)

# ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#### OTHER ALGORHYTMS TO TRY 68,81,225

### Values for when the coin isn't reflective (low light)
llo_h = 45
llo_s = 54
llo_v  = 150

lhi_h = 68
lhi_s = 81
lhi_v  = 225

### Values for when the coin IS reflective (low light)
blo_h = 45
blo_s = 54
blo_v  = 150

bhi_h = 68
bhi_s = 81
bhi_v  = 225


# HIGH LIGHT RANGE
# lower = np.array([220, 219, 215])
# upper = np.array([255, 255, 255])

# LOW LIGHT RANGE
lower = np.array([llo_h, llo_h, llo_v])
upper = np.array([lhi_h, lhi_s, lhi_v])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower, upper)

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

