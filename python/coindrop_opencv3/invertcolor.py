import cv2
import numpy as np

abc = cv2.imread('capture_hb/cam7.jpg')

(x1, y1) = abc.shape[:2]


target = abc[:,:,[1,2,0]]


if (abc == target).all():
    print("equal/match")

cv2.namedWindow('target',cv2.WINDOW_NORMAL)
cv2.resizeWindow('target', 1080,811)
cv2.imshow('target', target)
cv2.imwrite("target.jpg", target)
cv2.waitKey(0)
cv2.destroyAllWindows()