import cv2

cv2.namedWindow("klon")
img=cv2.imread("a.png")

img=cv2.resize(img,(1000,750))
cv2.imshow("klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()