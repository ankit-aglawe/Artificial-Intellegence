import numpy as np

import cv2 as cv

img = cv.imread('apple.jpg')

dst = cv.resize(img, None, fx=2,fy=2, interpolation= cv.INTER_CUBIC)

cv.imshow('resizeApple', dst)

cv.waitKey(0)
