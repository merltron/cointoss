#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# Read image
img = cv2.imread('capture/image40.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_TOZERO_INV)
# ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
# blur = cv2.GaussianBlur(im,(5,5),0)
# ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

## global thresholding
# gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(im,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

## adaptive thresholding
# th3 = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#            cv2.THRESH_BINARY,11,2)

## Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

## Change thresholds
params.minThreshold = 60
params.maxThreshold = 200

## Filter by Area.
params.filterByArea = True
params.minArea = 20
params.maxArea = 600

## Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.50

## Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.89

## Filter by Color
# filterByColor = 1
# blobColor = 255
    
## Filter by Inertia
# params.filterByInertia = True
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
print pointflag
if pointflag == 1 :
	print keypoints
	print "there's a coin"
elif pointflag > 1 :
	print keypoints
	print "a coin and something else"
else :
	print "nothing there"
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(thresh, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

