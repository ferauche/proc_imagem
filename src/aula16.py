import cv2

img1 = cv2.imread("../imgs/qrcode.png", 0) #original
img2 = cv2.imread("../imgs/qrcode_pic1.jpeg", 0) #comparada

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow("ORB", img3)
cv2.waitKey(0)