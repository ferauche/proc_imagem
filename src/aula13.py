import cv2

img = cv2.imread('../imgs/Eiffel.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#pode passar como parametro ao create a quantidade de features
sift = cv2.SIFT_create(200)

kp = sift.detect(gray, None)

#img = cv2.drawKeypoints(gray, kp, img)

img = cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Eiffel KPs", img)
cv2.waitKey(0)