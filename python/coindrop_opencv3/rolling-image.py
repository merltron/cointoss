import numpy as np
import cv2
import msvcrt

from time import sleep

img = cv2.imread('ourimg/image1.jpg',0)

i=0

def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret

try:
       while i < 6:
        if kbfunc():
            print(kbfunc())
        print(i)
        cv2.imwrite('messi{0}.png'.format(i), img)
        # Wait for the automatic gain control to settle
        sleep(2)
        # k = cv2.waitKey(0)
        if kbfunc() == ord('s'):  # wait for 's' key to save and exit
            cv2.destroyAllWindows()
            break
        elif i == 5:
            i = 0 # restart the loop
            continue
        else:
            i += 1
except KeyboardInterrupt:
    pass