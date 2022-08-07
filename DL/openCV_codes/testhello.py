# 系统默认的python版本为python3.7(global)

import cv2
import matplotlib
import matplotlib.pylab as plt
import numpy as np

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('01_cat.jpg')
print(img.shape)
# cat = img[0:200, 0:200]     # ROI

cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 1
cv_show('red', cur_img)

# cv_show('image', cat)
img_gray = cv2.imread('01_cat.jpg', cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)

cv2.imwrite('cat_gray.jpg', img_gray)

print(type(img))