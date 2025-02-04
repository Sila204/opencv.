import cv2
import numpy as np

img=cv2.imread("a.png")


dimension=img.shape
print(dimension)

color=img[150,200]
print("BGR:",color)

blue=img[420,500,0]
print("blue:",blue)

green=img[420,500,1]
print("green:",green)

red=img[420,500,2]
print("red:",red)

img[420,500,0]=250
print("new blue",img[420,500,0])

cv2.imshow("klon asker",img)
cv2.waitKey(0)
cv2.destroyAllWindows()