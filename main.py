import numpy as np
import cv2

# create 512x512 black images 
img = np.zeros((512, 512, 3), np.uint8)
img_rec = np.zeros((512, 512, 3), np.uint8)

# draw circle and rectangle on black images 
img1 = cv2.circle(img, (256, 256), 63, (255, 255, 255), -1)
img2 = cv2.rectangle(img_rec, (130, 130), (382, 382), (255, 255, 255), -1)


# logical operations on images 
# AND Operation 
img3 = cv2.bitwise_and(img1, img2)
# OR Operation 
img4 = cv2.bitwise_or(img1, img2)
# XOR Operation 
img5 = cv2.bitwise_xor(img1, img2)
# NOT Operation 
img6 = cv2.bitwise_not(img1)
img7 = cv2.bitwise_not(img2)

# showing images 
cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND Operation", img3)
cv2.imshow("OR Operation", img4)
cv2.imshow("XOR Operation", img5)
cv2.imshow("NOT img1", img6)
cv2.imshow("NOT img2", img7)

cv2.waitKey(0)
cv2.destroyAllWindows()

