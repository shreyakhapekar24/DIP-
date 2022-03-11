import cv2
import numpy as np

#read an image
img = cv2.imread("img1.jpg")

img_crop = img[0:300, 0:500]

cv2.imshow("window", img_crop)
cv2.waitKey(0)