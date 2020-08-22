import cv2

im = cv2.imread("../imgs/canal6.jpg")
'''
cortando a imagem
im_nova = im[0:600,693:]
'''

#redimensionando a imagem
'''
largura = im.shape[0]
altura = im.shape[1]
proporcao = largura / altura
n_largura = 480
n_altura = int(n_largura * proporcao)
im_nova = cv2.resize(im, (n_largura,n_altura),interpolation=cv2.INTER_AREA)
print(list(im_nova.shape))
'''
#espelhamento Transformada geometrica, alterando matriz identidade
'''
im_nova = im[:,::-1]
'''

#Rotacionamento
'''
(alt, lar) = im.shape[:2]
centro = (lar //2, alt //2)

M = cv2.getRotationMatrix2D(centro, 30, 1.0)
im_nova = cv2.warpAffine(im, M, (lar, alt))
'''

cv2.imshow("Imagem nova", im_nova)
cv2.waitKey(0)

