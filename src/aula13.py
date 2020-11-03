import cv2

gray = cv2.imread('../imgs/Eiffel.jpg', 0)

sift = cv2.SIFT()

kp = sift.detect(gray, None)

img = cv2.drawKeypoints(gray, kp)

cv2.imshow("Eiffel KPs", img)
cv2.waitKey(0)