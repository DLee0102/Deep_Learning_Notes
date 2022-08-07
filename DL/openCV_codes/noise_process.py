import cv2
import matplotlib
import matplotlib.pylab as plt
import numpy as np

# 二值化(或先转化为灰度图)后再来提取噪点信息？

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('04_LenaNoise.png')

#均值滤波，构造卷积核
blur = cv2.blur(img, (3, 3))
# cv_show('blur', blur)

# 方框滤波（和均值滤波类似）
box = cv2.boxFilter(img, 0, (3, 3), normalize=True)    # normalize指是否做归一化（即是否求均值），负一是通道数
# cv_show('box', box)

# 高斯滤波
gaussian = cv2.GaussianBlur(img, (3, 3), 1)
# cv_show('gaussian', gaussian)

# 中值滤波
median = cv2.medianBlur(img, 5)
# cv_show('median', median)
# noise = img - median
# cv_show(',', noise)

res = np.hstack((img, blur, gaussian, median))
cv_show('res', res)


