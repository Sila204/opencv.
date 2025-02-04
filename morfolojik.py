from pickletools import uint8

import cv2
import numpy as np

img=cv2.imread("1.webp")
kernel=np.ones((10,10),np.uint8)
erosion=cv2.erode(img,kernel,iterations=5)
dilation=cv2.dilate(img,kernel,iterations=5)  #kalınlaştırır
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) #gurultu silinir
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gardient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

cv2.imshow("img",img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gardient",gardient)
cv2.imshow("tophat",tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()

