import cv2
import numpy as np

img=cv2.imread("1.webp",0)
row,col=img.shape

M=cv2.getRotationMatrix2D((col/2,row/2),90,1)

dst=cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)
cv2.waitKey(0)