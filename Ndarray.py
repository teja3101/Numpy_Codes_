import numpy as np
ar = np.array([1,2,34,6,7,8,9,7,5,4])
print(ar.size)

ar_sum = ar.sum()
print(ar_sum)
print(ar.mean())
print("-----------------------------------------------")


ar1 = np.array(
    [
        [1,2],
        [3,4],
        [5,6]
    ]
)
print(ar1.size)               #total number of element
print(ar1.shape)              #number of rows and clms
print(ar1.itemsize)           #single item size in byte