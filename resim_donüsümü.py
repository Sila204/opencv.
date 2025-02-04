import cv2
import numpy as np

img=cv2.imread("1.webp",0)
row,col=img.shape

M=np.float32([[1,0,150],[0,1,200]])

dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)