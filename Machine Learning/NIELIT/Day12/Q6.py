import numpy as np
import cv2 as cv


licence_cascade=cv.CascadeClassifier('haarcascade_russian_plate_number.xml')

img=cv.imread('index.jpeg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

licence=licence_cascade.detectMultiScale(gray,1.25)


for (x,y,w,h) in licence:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow('name', img)
cv.waitKey(0)
