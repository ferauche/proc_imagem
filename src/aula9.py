import cv2
import numpy as np

img = cv2.imread("../imgs/moedas_2.jpeg")
#segmentacao por cor
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

for y in range(0, img_hsv.shape[0]):
   for x in range(0, img_hsv.shape[1]):
        (h, s, v) = img_hsv[y, x]
        img_hsv[y,x] = (0,0,v)

img_grayscale = cv2.cvtColor(img_hsv,cv2.COLOR_BGR2GRAY)
(T, img_bin) = cv2.threshold(img_grayscale,0,255,cv2.THRESH_OTSU)

cv2.imshow("Imagem normal", img)
cv2.imshow("Imagem convertida", img_hsv)
cv2.imshow("Imagem Escala de cinza", img_grayscale)
cv2.imshow("Imagem binarizada", img_bin)
cv2.waitKey(0)

sobelX = cv2.Sobel(img_bin, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img_bin, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Imagem segmentada", sobel)
cv2.waitKey(0)