import numpy as np
import cv2 as cv

img = cv.imread('apple.jpg',0)

rows,cols = img.shape

I = np.float32([[1,0,200],[0,1,100]])

dst = cv.warpAffine(img, I, (cols,rows))

cv.imshow('apple', dst)

cv.waitKey(0)



#-----------------------------------------------
