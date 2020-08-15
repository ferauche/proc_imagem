import cv2

#carrega um objeto imagem com suas características
#imagem = cv2.imread("../imgs/entrada.jpg")

#carrega um objeto imagempb em escala de cinza
imagempb = cv2.imread("../imgs/entrada.jpg",0)
print(list(imagempb.shape))
print(list(imagempb))

#exibe atributos de forma da imagem
#print('Largura em pixels: '+str(imagem.shape[1]))
#print('Altura em pixels: '+ str(imagem.shape[0]))
#print('Quantidade de canais: '+ str(imagem.shape[2]))

#lista a matriz de pixel e suas características
print("Imagem colorida")
print(list(imagem.shape))
print(list(imagem))
'''
print("Imagem pb")
print(list(imagempb))
'''
#(b, g, r) = imagem[0,0] # ordem BGR e não RGB CUIDADO!
#print("Pixel 0,0")
#print('Vermelho=', r)
#print('Verde=', g)
#print('Azull=', b)

#exibe a imagem
#cv2.imshow("Mapa da Ilha de S Vicente", imagem)
#cv2.waitKey(0)
'''
cv2.imshow("Mpara da Ilha de S Vicente PB", imagempb)
cv2.waitKey(0)
'''
#for y in range(0, imagem.shape[0]):
#    for x in range(0, imagem.shape[1]):
#        (b, g, r) = imagem[y, x]
#        imagem[y,x] = (b,g,0)

#cv2.imshow("Mapa alterado", imagem)
#cv2.waitKey(0)



