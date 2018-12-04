import numpy as np
import cv2 as cv

img = cv.imread('opencvlogo.png')

blur = cv.blur(img,(6,6))

cv.imshow('name', blur)
cv.waitKey(0)




img1 = cv.imread('face.jpg')

blur1 = cv.blur(img1,(6,6))

cv.imshow('name', blur1)
cv.waitKey(0)
