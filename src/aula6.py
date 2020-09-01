import cv2
import numpy as np

img = cv2.imread('../imgs/monalisa.jpg')


'''
cv2.imshow("Imagem Original",img)
suavizada = cv2.blur(img,(3,3))
cv2.imshow('Imagem Suavizada 3x3', suavizada)
'''

#juntando as imagens
'''
img = img[::2,::2] #Diminiu a imagem

suave = np.vstack([
    np.hstack([img, cv2.blur(img,(3,3))]),
])
cv2.imshow("Imagens",suave)
'''
cv2.waitKey(0)