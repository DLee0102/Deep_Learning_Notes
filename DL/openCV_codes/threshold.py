import cv2
import matplotlib
import matplotlib.pylab as plt
import numpy as np

# ret, dst = cv2.threshold(src, thresh, maxval, type)
# src:单通道图像; thresh:阈值; dst:输出图; maxval:当像素值超过了阈值（或小于阈值，根据type来决定），所赋予的值
# type:二值化操作的类型，包含以下5种类型：...; ret:阈值

img_gray = cv2.imread('01_cat.jpg', cv2.IMREAD_GRAYSCALE)

ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)


titles = ['Original Image', 'Binary', 'Binary_Inv', 'Trunc', 'Tozero', 'Tozero_Inv']

images = [img_gray, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
