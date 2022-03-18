import cv2 as cv

img = cv.imread('img5.jfif')
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

cv.waitKey(0)