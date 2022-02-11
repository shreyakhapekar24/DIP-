import cv2

originalImage = cv2.imread('nature.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

subtrctImage = grayImage - blackAndWhiteImage

cv2.imshow('Black White Image', blackAndWhiteImage)
cv2.imshow('Original Image', originalImage)
cv2.imshow('Gray Image', grayImage)
cv2.imshow('Subtracted Image', subtrctImage)

cv2.waitKey(0)
cv2.destroyAllWindows()