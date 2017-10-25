# USAGE
# python detect_circles.py --image images/simple.png

# import the necessary packages
import numpy as np
import argparse
import cv2
print cv2.__version__
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
image = cv2.imread("D:\_OPENCV\coindrop\demo\circle-detection-opencv\ourimg\image1tm-onlycoin.jpg")
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
							   cv2.THRESH_BINARY_INV, 11, 1)

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
						   kernel, iterations=4)

cont_img = closing.copy()
# contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,
#									   cv2.CHAIN_APPROX_SIMPLE)

# detect circles in the image
circles = cv2.HoughCircles(cont_img, cv2.cv.CV_HOUGH_GRADIENT, 2, 100.0, 30, 150,25,45)
print circles
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")

	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

	# show the output image
	cv2.imshow("output", np.hstack([output]))
	cv2.waitKey(0)