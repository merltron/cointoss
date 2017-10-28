import numpy as np
import cv2
import msvcrt
from time import sleep
import glob

def checkmatch(x) :

    if x in (28, 29):
        return 1
    else :
        return 0

### Cycle through the images
try:
       poscount = 0
       x = 21
       while x < 31:
        # cv2.imwrite('messi{0}.png'.format(i), img)
        # Wait for the automatic gain control to settle
        sleep(2)

        # Check if x is even
        print "Assessing file: image%s.jpg" % str(x)
        print "Comparing " + str(x) + " to " + str(poscount)

        result = checkmatch(x)

        if result == 1 :
            print "Caught one!!"
            poscount = poscount + 1

        print "poscount is now:" + str(poscount)

        if poscount == 2:
            print "BOMBS AWAY!!"
            poscount = 0

        if x == 30:
            x = 21 # restart the loop
            continue
        else:
            x += 1
except KeyboardInterrupt:
    pass