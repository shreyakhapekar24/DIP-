import cv2
import numpy as np

#read an image
img = cv2.imread("img1.jpg")

img_flip = cv2.flip(img, -1)

cv2.imshow("window", img_flip)

cv2.waitKey(0)