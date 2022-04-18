# Step-1 : Load libraries and image 

from unicodedata import name
from matplotlib import scale
import numpy as np
import cv2

# read image 
img = cv2.imread("girl.jpg")
img = cv2.resize(img, (800, 700))

# create Trackbar-----
def nothing(x):
    pass

# window name
cv2.namedWindow("Color Adjustments", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustments", (300, 300))
cv2.createTrackbar("Scale", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Color", "Color Adjustments", 0, 255, nothing)

# Step-2 
# convert into gray 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


while True:
    scale = cv2.getTrackbarPos("Scale", "Color Adjustments")
    clr = cv2.getTrackbarPos("Color", "Color Adjustments")  #getting track bar value


    # Extracting color code 
    # Step-3 : Inverted gray scale image (for shifting toward selected channel)

    inverted_gray = clr - gray   #inverted color image

    # Step-4 : Apply image smooting for Shading effect 

    blur_img = cv2.GaussianBlur(inverted_gray, (21, 21), 0)


    # Step-5 : Invert Blur Image and Apply division between gray and invert_blur.

    inverted_blur = clr - blur_img   #inverted blured image
    fltr = cv2.divide(gray, inverted_blur, scale = scale)




    # Output-------
    cv2.imshow("opt", fltr)
    k = cv2.waitKey(1)

    if k == ord("q"):
        break

    if k == ord("s"):
        cv2.imwrite("res.jpg", fltr)


cv2.destroyAllWindows()
























