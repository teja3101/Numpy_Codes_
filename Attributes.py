import numpy as np
arr = np.array([1,2,3,4,5])
arr1 = np.array(
    [
        [1,2],
        [3,4],
        [5,5]
    ]
) 
print(arr1.shape)                          #rows and clms
print(arr1.ndim)                           #dimension
print(arr1.dtype)                          #datatype
print(arr1.strides)                        #total bytes and then element present in arr each ele's bytes
print(arr1.flags)                          #gives info about memory and other