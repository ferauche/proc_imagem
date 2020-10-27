import cv2
import numpy as np

img = cv2.imread('../imgs/chessboard2.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img32 = np.float32(gray)

dst = cv2.cornerHarris(img32,4,9,0.05)
dst = cv2.dilate(dst,None)

#
img[dst>0.1*dst.max()] = [0,0,255]

cv2.imshow('Cantos', img)

cv2.waitKey(0)