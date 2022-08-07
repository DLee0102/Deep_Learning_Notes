import cv2
import matplotlib
import matplotlib.pylab as plt
import numpy as np

img_cat = cv2.imread('01_cat.jpg')
img_dog = cv2.imread('03_dog.jpg')

img_dog = cv2.resize(img_dog, (500, 414))
res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)
plt.imshow(res)
plt.waitforbuttonpress()
