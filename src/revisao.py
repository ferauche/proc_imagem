import cv2

img = cv2.imread("../imgs/perfil.jpg",0)
img_blur = cv2.GaussianBlur(img, (11,11),0)
(T, img_bin) = cv2.threshold(img_blur, 230, 255, cv2.THRESH_BINARY)
img_adapt = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,0)
(T, otsu) = cv2.threshold(img_blur, 0, 255, cv2.THRESH_OTSU)

largura = img.shape[0]
altura = img.shape[1]
proporcao = largura / altura
n_largura = 640
n_altura = int(n_largura * proporcao)
im_nova = cv2.resize(img, (n_largura,n_altura),interpolation=cv2.INTER_CUBIC)
cv2.imshow("perfil", img_bin)
cv2.imshow("perfil2", img_adapt)
cv2.imshow("perfil3", otsu)
cv2.imshow("perfil4", im_nova)
cv2.waitKey(0)