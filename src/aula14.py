import cv2

img1 = cv2.imread("../imgs/Eiffel4.jpg",0)  #queryImage
img2 = cv2.imread("../imgs/Eiffel_model.jpg",0) #trainImage

sift = cv2.SIFT_create(150)

kp1, desc1 = sift.detectAndCompute(img1,None)
kp2, desc2 = sift.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(desc1, desc2)
matches = sorted(matches, key = lambda x : x.distance)
for d in matches:
    print(d.distance)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, img2, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

'''
bf = cv2.BFMatcher()
matches = bf.knnMatch(desc1, desc2, k=2)
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
'''
cv2.imshow("Matches",img3)
cv2.waitKey(0)