import cv2

img = cv2.imread('ebook.png', 1)
cropped_img = img[100: 145, 0: 239]
cv2.imshow('Test Image', cropped_img)
cv2.imwrite('crop.png', cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

