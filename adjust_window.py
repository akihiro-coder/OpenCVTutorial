"""ウインドウの調整"""


import cv2


# img = cv2.imread('./images/data/src/Lena.jpg')
# cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('window', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# img = cv2.imread('./images/data/src/Lena.jpg')
# cv2.namedWindow('window', cv2.WINDOW_NORMAL)
# cv2.imshow('window', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



img = cv2.imread('./images/data/src/Lena.jpg')
cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('window', 1000, 1000)
cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
