"""動画の表示・出力"""


import cv2
import sys


cap = cv2.VideoCapture('./images/data/movie/Cosmos.mp4')
if cap.isOpened() == False:
    sys.exit()

ret, frame = cap.read() # 1フレームだけ読み込む, ret: 読み込み成功True
h, w = frame.shape[:2] # 画像サイズを取得　
fourcc = cv2.VideoWriter_fourcc(*"XVID") # 書き込みの設定
dst = cv2.VideoWriter('./images/output/test.avi', fourcc, 30.0, (w, h)) # 30.0: fps




while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow('img', frame)
    dst.write(frame)
    if cv2.waitKey(30) == 27: # 30ms待つ、27: escape key
        break
cv2.destroyAllWindows()
cap.release() # free memory