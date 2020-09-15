import cv2


img = cv2.imread('../imgs/canal6.jpg',0)
img = img[::2,::2]

cv2.imshow("Escala de Cinza", img)

suave = cv2.GaussianBlur(img, (5,5),0)
cv2.imshow("Suavizacao Gaussiana", suave)

(T, bin) = cv2.threshold(suave, 150, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 150, 255, cv2.THRESH_BINARY_INV)

bin_adap = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY_INV, 21, 0)

cv2.imshow("Binarizada", bin)
cv2.imshow("Binarizada Inv", binI)
cv2.imshow("Binarizada Adpt Media", bin_adap)
cv2.waitKey(0)