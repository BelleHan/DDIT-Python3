import cv2

img = cv2.imread('b.png', 1)
print(img)
cv2.imshow('Test Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# [[[ 36  30 238]]]
# [[[ 77 177  36]]]
# [[[204  79  72]]]