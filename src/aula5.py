from matplotlib import pyplot as plt

import cv2

img = cv2.imread('../imgs/entrada.jpg')

#Histograma PB
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Imagem", img)

h = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histograma PB")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0,256])
plt.show()
'''
#Histograma Colorido
canais = cv2.split(img)
cores = ("b", "g", "r")
plt.figure()
plt.title("Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Numero de Pixels")
for (canal, cor) in zip(canais, cores):
    hist = cv2.calcHist([canal],[0], None, [256], [0, 256])
    plt.plot(hist, color=cor)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
'''
'''
#deixando mais escura a imagem
for y in range(0, img.shape[0]):
   for x in range(0, img.shape[1]):
        img[y,x] = img[y,x] //4

cv2.imshow("Imagem escurecida", img)
plt.figure()
plt.title("Imagem escurecida")
plt.xlabel("Intensidade")
plt.ylabel("Pixels")
plt.hist(img.ravel(),256,[0,256])
plt.xlim([0,256])
plt.show()
#equalizacao PB

equalizado = cv2.equalizeHist(img)

plt.figure()
plt.title("Imagem equalizada")
plt.xlabel("Intensidade")
plt.ylabel("Pixels")
plt.hist(equalizado.ravel(),256,[0,256])
plt.xlim([0,256])
plt.show()

cv2.imshow("Equalizada", equalizado)
'''
cv2.waitKey(0)
