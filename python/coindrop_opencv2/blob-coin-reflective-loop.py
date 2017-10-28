#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import glob
# import RPi.GPIO as GPIO
from time import sleep


################################# IMAGE CHECK
def checkmatch(myimg) :
    print "Assessing file: image{0}.jpg".format(myimg)
    image = cv2.imread('capture/reflective-test-set/image{0}.jpg'.format(myimg))
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    th, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_TOZERO_INV)
    # ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #### OTHER ALGORHYTMS TO TRY
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
    params.minThreshold = 100
    params.maxThreshold = 200

    ## Filter by Area.
    params.filterByArea = True
    params.minArea = 20
    params.maxArea = 600

    ## Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.85

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
        return 1
    elif pointflag > 1 :
        print keypoints
        return 2
    else :
        return 0
    ###### Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    # im_with_keypoints = cv2.drawKeypoints(thresh, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    ###### Show blobs
    # cv2.imshow("Keypoints", im_with_keypoints)
    # cv2.waitKey(0)

################################# DROP THE COIN

def dropcoin(myimg) :
    print myimg

    # The script as below using BCM GPIO 00..nn numbers
    # GPIO.setmode(GPIO.BCM)

    # Set relay pins as output
    # GPIO.setup(18, GPIO.OUT)
    # GPIO.setup(23, GPIO.OUT)
    # GPIO.setup(24, GPIO.OUT)
    # GPIO.setup(25, GPIO.OUT)

    # while (True):
    #     # Turn all relays ON
    #     GPIO.output(18, GPIO.HIGH)
    #     GPIO.output(23, GPIO.HIGH)
    #     GPIO.output(24, GPIO.HIGH)
    #     GPIO.output(25, GPIO.HIGH)
    #     # Sleep for 5 seconds
    #     sleep(5)
    #     # Turn all relays OFF
    #     GPIO.output(18, GPIO.LOW)
    #     GPIO.output(23, GPIO.LOW)
    #     GPIO.output(24, GPIO.LOW)
    #     GPIO.output(25, GPIO.LOW)
    #     # Sleep for 5 seconds
    #   sleep(5)


    return

################################# Cycle Section

### Cycle through the images
try:
       poscount = 0
       x = 21
       while x < 31:

        print "Comparing " + str(x) + " to " + str(poscount)

        # Send the image for coin recognition
        result = checkmatch(x)

        # Wait for the automatic gain control to settle
        sleep(2)

        # Asess if the coin was recognized
        if result == 1 :
            print "Caught one!!"
            poscount = poscount + 1
        elif result == 2 :
            print "Multiple things that could be a coin"
        else :
            print "Found nothing"

        print "poscount is now:" + str(poscount)

        # Check if coin was recognized in enough frames
        if poscount == 2:
            dropcoin("BOMBS AWAY!!")
            poscount = 0

        if x == 30:
            x = 21 # restart the loop
            continue
        else:
            x += 1
except KeyboardInterrupt:
    pass
