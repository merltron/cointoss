#!/usr/bin/env python
# -*- coding: utf-8 -*-
# returns HSV value of the pixel under the cursor in a video stream
# author: achuwilson
# achuwilson.wordpress.com
import cv2
import time
x_co = 0
y_co = 0
def on_mouse(event,x,y,flag,param):
  global x_co
  global y_co
  if(event==cv2.EVENT_MOUSEMOVE):
    x_co=x
    y_co=y

cv2.namedWindow("camera", 1)
capture = cv2.imread('capture_hb/cam4.jpg',1)

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 0.5
fontcolor = (255, 255, 255)

src = capture
cv2.blur(src,(3,3))

hsv = cv2.CreateImage(cv2.GetSize(src), 8, 3)
thr = cv2.CreateImage(cv2.GetSize(src), 8, 1)

cv2.cvtColor(src, hsv, cv2.COLOR_BGR2HSV)
cv2.setMouseCallback("camera",on_mouse, 0)

s=cv2.get2d(hsv,y_co,x_co)

print("H:",s[0],"      S:",s[1],"       V:",s[2])
cv2.putText(src,str(s[0])+","+str(s[1])+","+str(s[2]), (x_co,y_co),fontface, (55,25,255))
cv2.imshow("camera", src)
cv2.waitKey(0)
