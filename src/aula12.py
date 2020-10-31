import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../imgs/chessboard.jpeg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img_gray, 81, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

#plt.imshow(img),plt.show()
cv2.imshow("Chess",img)
cv2.waitKey(0)