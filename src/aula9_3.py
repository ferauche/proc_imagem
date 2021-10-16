import numpy as np
import cv2
img = cv2.imread("../imgs/moedas_2.jpeg",0)
img_blur = cv2.GaussianBlur(img, (11,11),0)

canny1 = cv2.Canny(img_blur, 100, 240)

cv2.imshow("Canny ", canny1)
cv2.waitKey(0)