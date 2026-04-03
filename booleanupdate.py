import numpy as np
arr = np.array([1,2,4,5,6,0,8,9])
arr[arr>=4] = 31
print(arr)