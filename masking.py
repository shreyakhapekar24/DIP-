import cv2 as cv
from cv2 import rectangle
import numpy as np

img = cv.imread("img2.jpg")
cv.imshow("Original Image", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank image", blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Circle Mask", circle)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow("Rectangle Mask", rectangle)

weird = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shaped Mask", weird)

circle_masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Circle Masked Image", circle_masked)

rect_masked = cv.bitwise_and(img, img, mask=rectangle)
cv.imshow("Rectangle Masked Image", rect_masked)

weird_masked = cv.bitwise_and(img, img, mask=weird)
cv.imshow("Weird Masked Image", weird_masked)

cv.waitKey(0)