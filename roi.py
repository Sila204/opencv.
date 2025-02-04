#roi --> region of interest --> ilgi alani
import cv2

img=cv2.imread("a.png")
print(img.shape[:2])

roi=img[20:280,200:400]


cv2.imshow("klon",img)
cv2.imshow("roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()