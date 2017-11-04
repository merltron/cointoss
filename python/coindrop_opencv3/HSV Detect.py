import numpy as np
import cv2

img = cv2.imread('capture_hb/cam7.jpg'

# Make a copy of the original image
wokingcopy = img.copy();

# Convert RGB to HSV
hsv_img = cv2.cvtColor(wokingcopy,cv2.COLOR_BGR2HSV));

# .To access each pixel in the images we are using this syntax:
# .image.at(y,x)[c] where y is the row, x is the column
# .and c is H, S or V (0, 1 or 2)
Vec3b p = HSV_image_display.at<Vec3b>(50, 10); # .Vec3b - Array of 3 uchar numbers

# .p[0] - H, p[1] - S, p[2] - V
printf(text, "H=%d, S=%d, V=%d", p[0], p[1], p[2]);

# .putText(matSrcCopyForHSVColorDisplay, text, Font_Position,
# .Font_Type, Font_Scale, Font_Colour, Font_Thickness);
# .Display the text
putText(matSrcCopyForHSVColorDisplay, text, center,
        FONT_HERSHEY_COMPLEX_SMALL, 2, cvScalar(255, 0, 0), 1, CV_AA);

# .Refresh the image
imshow("HSV Value", matSrcCopyForHSVColorDisplay);
printf("H=%d, S=%d, V=%d\n", p[0], p[1], p[2]);