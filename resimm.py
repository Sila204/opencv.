import cv2

img=cv2.imread("a.png")
#print(img)

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.imwrite("a.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()