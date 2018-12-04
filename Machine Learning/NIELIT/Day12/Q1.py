import numpy as np
import cv2 as cv

img = cv.imread('gradient.jpg')

ret, dt1 = cv.threshold(img, 127,255,cv.THRESH_BINARY)
cv.imshow('name', dt1)
cv.waitKey(0)


ret, dt2 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV)
cv.imshow('name', dt2)
cv.waitKey(0)



ret, dt3 = cv.threshold(img, 127,255,cv.THRESH_TRUNC)
cv.imshow('name', dt3)
cv.waitKey(0)



ret, dt4 = cv.threshold(img, 127,255,cv.THRESH_TOZERO)
cv.imshow('name', dt4)
cv.waitKey(0)


ret, dt5 = cv.threshold(img, 127,255,cv.THRESH_TOZERO_INV)
cv.imshow('name', dt5)
cv.waitKey(0)
