import numpy as np
import cv2 as cv

img = cv.imread('man.jpg')

kernel =np.ones((2,2),np.uint8)

op = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
op1 = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)


v = np.hstack((op,op1))
cv.imshow('name',v)

cv.waitKey(0)
