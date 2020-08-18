import cv2

imagem = cv2.imread("../imgs/cockpit.jpg")
print(list(imagem.shape))
#seta todos os pixels entre as linhas 100,150 ate o final para a cor vermelha
#lembre-se (b,g,r)
imagem[100:120, : ] = (0,0,255)

#seta todos os pixels entre as colnas 50 e 100 de verde
imagem[ : , 50:100] = (0,255,0)

#seta todos os pixels entre as linhas 200 e 250 e colunas 150, 200
imagem [200:250,150:200] = (0,0,0)

#desenhando uma linha
cv2.line(imagem,(0,0),(400,400), (255,255,255),2)
cv2.rectangle(imagem,(300,200),(350,300),(0,0,0),-1)
cv2.circle(imagem,(160,200),150,(114,114,114),4)

fonte = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(imagem, 'Processamento de Imagem',
            (10,30), fonte, 1,
            (255,255,255))



cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

