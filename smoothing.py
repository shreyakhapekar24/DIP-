import cv2 as cv
from cv2 import GaussianBlur

img = cv.imread("img5.jfif")
cv.imshow("Original Image", img)

# Averaging 
average = cv.blur(img, (7, 7))
cv.imshow("Average Blur", average)

# Gaussian Blur 
# less blur than average 
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur 
median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

# Bilateral 
# most effective as it retains the edges
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)