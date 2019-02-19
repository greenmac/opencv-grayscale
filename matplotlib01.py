import cv2.cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axisplt.plot([200,300,400],[100,200,300],'c', linewidth=5)plt.show()
cv2.imwrite('watchgray.png',img)