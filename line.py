import cv2
import numpy as np

img = cv2.imread("img1.jpg", 1)

img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
img = cv2.arrowedLine(img, (0,255), (255, 255), (255, 0, 0), 10)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()