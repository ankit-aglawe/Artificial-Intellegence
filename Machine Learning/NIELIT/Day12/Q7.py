import numpy as np
import cv2 as cv


img = cv.imread('messi.jpg',0)

edges = cv.Canny(img,100,200)

img1 = np.hstack((img,edges))

cv.imshow('name',img1)
cv.waitKey(0)
