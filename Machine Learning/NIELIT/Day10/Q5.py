import numpy as np
import cv2 as cv

img =cv.imread('orange.jpg',0)

#img[:,:]=img[:,:]-255

#img = cv.bitwise_not(img)


img = 255-img

cv.imshow('neg',img)

cv.waitKey(0)
