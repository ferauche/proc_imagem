import numpy as np
import cv2

img = cv2.imread('../imgs/moedas_1.jpeg',0)
blur = cv2.blur(img, (5,5))

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imshow("Filtro laplaciano", lap)
cv2.waitKey(0)