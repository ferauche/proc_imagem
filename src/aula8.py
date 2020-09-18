import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../imgs/monalisa.jpg',0)
img = img[::2,::2]

#binarizacao
(T, ibin) = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

#Otsu
(T2, ibin2) = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

#Otsu depois do suavizacao Gaussiana e após binarizacao
suave = cv2.GaussianBlur(img, (5,5),0)
(T3, ibin3) = cv2.threshold(suave, 0, 255, cv2.THRESH_OTSU)

#histogramas
himg = cv2.calcHist([img],[0],None, [256],[0, 256])
hbin = cv2.calcHist([suave],[0],None, [256],[0,256])
hbin2 = cv2.calcHist([ibin2],[0],None, [256],[0,256])
hbin3 = cv2.calcHist([ibin3],[0],None, [256],[0,256])

hists = [("Original PB", himg), ("Suavizada", hbin),
         ("Otsu", hbin2), ("Suavizado Otsu",hbin3)]


for h in hists:
    plt.figure()
    plt.title(h[0])
    plt.xlabel("Intensidade")
    plt.ylabel("Qtde de Pixels")
    plt.plot(h[1])
    plt.xlim([0,256])
    plt.show()

cv2.imshow("Original", img)
cv2.imshow("Binarizacao", ibin)
cv2.imshow("OTSU", ibin2)
cv2.imshow("Suavizacao+Otsu", ibin3)
cv2.waitKey(0)




