import cv2

# read two images 
img_1 = cv2.imread('b.img.png', cv2.IMREAD_COLOR)
img_2 = cv2.imread('g.img.png', cv2.IMREAD_COLOR)

# addition of gray and binary image 
img_3  = cv2.addWeighted(img_1, 0.5, img_2, 0.5, 0.0)

img_4 = 20 + img_2

# showing an output images 
cv2.imshow('added_image', img_3)
cv2.imshow('added_20', img_4)

cv2.waitKey(0)
cv2.destroyAllWindows()