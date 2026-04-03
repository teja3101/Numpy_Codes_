import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,0])
new_arr = np.concatenate((arr1,arr2),axis=0)
print(new_arr)

ar1 = np.array(
    [
        [2,3],
        [5,6]
    ]
)
ar2 = np.array(
    [
        [8,9],
        [7,5]
    ]
)
new = np.concatenate((ar1,ar2),axis=0)
print(new)