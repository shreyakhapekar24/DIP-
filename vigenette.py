import cv2
import numpy as np 

#reading the image and getting the properties
img = cv2.imread("girl.jpg")
rows, cols = img.shape[:2]

# generating vignette mask by using gaussian kernels 
kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)
kernel = kernel_y * kernel_x.T

# Normalizing the kernel 
kernel = kernel/np.linalg.norm(kernel)

# Generating a mask to image 
mask = 255 * kernel
output = np.copy(img)

# Applying the mask to each channel in the input image 
for i in range(3):
    output[:, :, i] = output[:, :, i] * mask
    
cv2.imshow("original", img)
cv2.imshow("Vignettte", output)
cv2.waitKey(0)
