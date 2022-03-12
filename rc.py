import cv2
from cv2 import imread
import numpy as np

img = imread("img2.jpg", 1)

img = cv2.rectangle(img, (384, 0), (510, 128), (0,0,255), 10)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

cv2.imshow("rectangle and circle on image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()