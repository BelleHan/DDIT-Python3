import cv2
import numpy as np

img = cv2.imread('r.png', 1)
print(img.shape)
arr = [
        [
            [36,30,238]
        ]
       ]

arr_n = np.array(arr)


print(img)
print(arr_n.shape)
print(arr_n)


cv2.imshow('Test Image', arr_n)



cv2.waitKey(0)
cv2.destroyAllWindows()
