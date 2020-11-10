import cv2

img = cv2.imread('../imgs/Eiffel.jpg',0)

sift = cv2.SIFT_create()
kp1 = sift.detect(img, None)

#start = cv2.xfeatures2d.StarDetector_create()
#kp1 = start.detect(img, None)

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp2, des = brief.compute(img,kp1)

img = cv2.drawKeypoints(img,kp2,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Brief",img)
cv2.waitKey(0)

print("Keypoint SIFT", len(kp1))
print("Keypoint Brief", len(kp2))
print("Tamanho Descriptor: ", brief.descriptorSize())
