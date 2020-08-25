import numpy as np
import cv2

img = cv2.imread('../imgs/canal6.jpg')
cv2.imshow("Original", img)

#mascara = np.full(img.shape[:2],0, dtype = "uint8")
#(cx, cy) = (img.shape[1]//2, img.shape[0]//2)
#cv2.circle(mascara, (cx, cy), 300, (255, 255, 255), -1)
#img_mascara = cv2.bitwise_and(img, img, mask = mascara)

#cv2.imshow("Imagem com máscara", img_mascara)
#cv2.waitKey(0)
#cv2.imwrite('../img/saida.jpg', img_mascara)

#conversao de espacos de cores
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("Escala de cinza", gray)
#cv2.imshow("HSV", hsv)
#cv2.waitKey(0)