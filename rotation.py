import cv2

img = cv2.imread("img3.jfif")

height, width, depth = img.shape

center = (width // 2, height // 2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
imgr = cv2.warpAffine(img, matrix, (width, height))

print(matrix)

#show rotated image
cv2.imshow("original", img)
cv2.imshow("rotated", imgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
