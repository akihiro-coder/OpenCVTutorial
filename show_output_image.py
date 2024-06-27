"""画像の表示・出力"""

import cv2
import os

img = cv2.imread('./images/data/src/Berry.jpg')
cv2.imshow('img', img)
cv2.waitKey(0) # 引数の数msだけ入力を受け付ける
cv2.destroyAllWindows()
os.mkdir('./images/output')
cv2.imwrite('./images/output/Berry.jpg', img)