import cv2
import math
import numpy as np

d_red = cv2.cv.RGB(150, 55, 65)
l_red = cv2.cv.RGB(250, 200, 200)

orig = cv2.imread("demo/circle-detection-opencv/ourimg/image1tm-onlycoin.jpg")
img = orig.copy()
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(img2, (15, 15), 0)
thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 1)

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
                           kernel, iterations=4)

cont_img = closing.copy()

detector = cv2.FeatureDetector_create('MSER')
fs = detector.detect(cont_img)
fs.sort(key = lambda x: -x.size)

def supress(x):
        for f in fs:
                distx = f.pt[0] - x.pt[0]
                disty = f.pt[1] - x.pt[1]
                dist = math.sqrt(distx*distx + disty*disty)
                if (f.size > x.size) and (dist<f.size/2):
                        return True

sfs = [x for x in fs if not supress(x)]

for f in sfs:
        cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(f.size/2), d_red, 2, cv2.CV_AA)
        cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(f.size/2), l_red, 1, cv2.CV_AA)

# h, w = orig.shape[:1]
# vis = np.zeros((h, w), np.uint8)
# vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
# vis[:h, :w] = img
# vis[:h, w+5:w*2+5] = img

cv2.imshow("image", img)
#cv2.imwrite("c_o.jpg", vis)
cv2.waitKey()
cv2.destroyAllWindows()