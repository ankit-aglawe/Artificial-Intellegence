import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


img = cv.imread('man.jpg')
kernal = np.ones((2,2),np.uint8)

erosion = cv.erode(img,kernal,iterations=1)

dilate=cv.dilate(img,kernal,iterations=2)

#cv.imshow('erosion',erosion)
#cv.imshow('dilate',dilate)

dil=cv.dilate(erosion,kernal,iterations=2)

v=np.hstack((img,erosion,dilate,dil))
#cv.imshow('combine',dil)
cv.imshow('combine',v)

cv.waitKey(0)
