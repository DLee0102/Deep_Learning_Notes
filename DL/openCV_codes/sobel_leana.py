import cv2
from cv2 import addWeighted
import matplotlib
import matplotlib.pylab as plt
import numpy as np

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('07_Lena.jpg',cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

res = addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv_show('edge', res)