import cv2

gray = cv2.imread('../imgs/Eiffel.jpg', 0)

#pode passar como parametro ao create a quantidade de features
sift = cv2.SIFT_create()

kp = sift.detect(gray, None)

img = cv2.drawKeypoints(gray, kp, gray)

cv2.imshow("Eiffel KPs", img)
cv2.waitKey(0)