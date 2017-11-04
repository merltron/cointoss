import numpy as np
import cv2

green = np.uint8([[[255,255,255]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
