import numpy as np

import cv2 as cv

img1 = cv.imread('apple.jpg')

img2 = cv.imread('orange.jpg')

halfImg = img2[:,img2.shape[0]/2:img2.shape[0]]

img1[:,img1.shape[0]/2:img1.shape[0]]= halfImg

cv.imshow('a', img1)

cv.waitKey(0)
