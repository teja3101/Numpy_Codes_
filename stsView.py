import numpy as np

arr = np.array([1,3,5,6,8,7,9,767,67,6,5,69])
arr1 = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)

# slicing
view = arr[1:7]
print(view)

view[1] = 31                         
print(arr)

# transpose
view1 = arr1.T
print(view1)

view1[0,1] = 31
print(arr1)

# reshaping
view2 = arr.reshape(3,4)
print(view2)

view2[0,3] = 21
print(arr)