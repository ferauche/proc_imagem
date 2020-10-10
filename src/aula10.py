import numpy as np
import cv2

img = cv2.imread("../imgs/moedas_2.jpeg",0)
img_blur = cv2.GaussianBlur(img, (7,7),0)


(T, img_bin) = cv2.threshold(img_blur,0,255,cv2.THRESH_OTSU)
canny = cv2.Canny(img_bin, 100, 200)
contornos, hierarquia = cv2.findContours(canny, cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_NONE)

print("Objetos encontrados: "+str(len(contornos)))

cpy_img = img.copy()

cv2.drawContours(cpy_img, contornos, -1, (0, 255, 0), 3)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", img_blur)
cv2.imshow("Imagem bin", img_bin)
cv2.imshow("Canny ", canny)
cv2.imshow("Bordas", cpy_img)
cv2.waitKey(0)