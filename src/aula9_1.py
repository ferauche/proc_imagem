import cv2
import numpy as np

img = cv2.imread('../imgs/moedas_1.jpeg',0)

blur = cv2.blur(img, (5,5))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("imagem sobel", sobel)
cv2.waitKey(0)