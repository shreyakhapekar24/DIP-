import cv2
import numpy as np 

#read image
src = cv2.imread('butterfly.jpg', cv2.IMREAD_UNCHANGED)
print(src.shape)

# extract green channel
blue_channel = src[:, :, 0]
green_channel = src[:, :, 1]
red_channel = src[:, :, 2]


# create empty image with same shape as that of src image
blue_img = np.zeros(src.shape)
green_img = np.zeros(src.shape)
red_img = np.zeros(src.shape)

# assign the green channel of src to empty image 
green_img[:, :, 1] = green_channel
blue_img[:, :, 0] = blue_channel
red_img[:, :, 2] = red_channel

# show image 
cv2.imshow('green channel', green_img)
cv2.imshow('blue channel', blue_img)
cv2.imshow('red channel', red_img)

cv2.waitKey(0)
