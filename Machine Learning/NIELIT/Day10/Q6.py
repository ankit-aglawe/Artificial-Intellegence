
import numpy as np

import cv2 as cv

from skimage.measure import structural_similarity as ssim

img1 = cv.imread('apple.jpg').astype(np.int8)

img2 = cv.imread('orange.jpg').astype(np.int8)

#print(img1)
#print(img2)
zeromatrix = (cv.imread('apple.jpg').astype(np.int8)-cv.imread('apple.jpg').astype(np.int8))

sub = img1-img2

#print(sub)


if (sub == zeromatrix).all():
    print('Image are same')
else:
    print('Images are different')
