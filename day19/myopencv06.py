import cv2

img = cv2.imread('ebook.png', 1)
cv2.imshow('Test Image', img)
cv2.imwrite('mine.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

