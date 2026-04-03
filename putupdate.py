import numpy as np
arr = np.array([1,2,3,4,5,6,8,7])
np.put(arr, [0,3,6],[31,21,52])
print(arr)