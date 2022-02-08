import cv2 
import numpy as np 

#read an image

img = cv2.imread("fruits.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img_gray.shape)

cv2.imshow("window", img_gray)

cv2.waitKey(0)