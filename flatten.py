import numpy as np
arr = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [8,9,5,6]
    ]
) 
arr[0][0] = 9
print(arr)
flat_obj = arr.flatten()
print(flat_obj)
