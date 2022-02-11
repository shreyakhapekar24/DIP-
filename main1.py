from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('img.baby.jpg')

R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
imgGray = 0.333 * R + 0.333 * G + 0.333 * B
plt.imshow(imgGray, cmap = 'gray')
plt.show()
