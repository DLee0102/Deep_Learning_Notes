import cv2
import matplotlib
import matplotlib.pylab as plt
import numpy as np

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('06_pie.png')

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  
# cv2.CV_64F是为了在np数值上保留负数值，但对于RGB图仍需作如下转换
sobelx = cv2.convertScaleAbs(sobelx)
# cv_show('sobel', sobelx)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

res = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv_show('edge', res)

