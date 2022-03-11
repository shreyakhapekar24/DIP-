import cv2
import numpy as np

#read an image

img = cv2.imread("img1.jpg")
img_resize = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv2.imshow("window", img_resize)

print(img_resize.shape)

cv2.waitKey(0)