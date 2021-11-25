import numpy as np


arr = [1,2,3,4,5,6]
arr_n = np.array(arr)

arr_n = arr_n.reshape(2,3)

print(arr_n)
print(arr_n.shape)