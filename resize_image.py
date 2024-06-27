"""画像のリサイズ"""

import cv2


img = cv2.imread('./images/data/src/grapes.jpg')
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# resize
size = (300, 200) # w, h
img_resize = cv2.resize(img, size) # w,hで渡す
print(img_resize.shape)

cv2.imshow('resized image', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()