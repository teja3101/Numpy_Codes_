import numpy as np

arr = np.array([1,2,3], dtype = 'i')
print("Before conversion nums are: ", arr)
print("Datatype of Before conversion nums is", arr.dtype)
print("----------------------------------------")
arr1 = arr.astype(np.float64)
print("After conversion nums are: ", arr1)
print("Datatype of After conversion nums is", arr1.dtype)
print("----------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


arr2 = np.array([21.31,2025.235,32.25], dtype = 'f')
print("Before conversion nums are: ", arr2)
print("Datatype of Before conversion nums is", arr2.dtype)
print("----------------------------------------")
arr3 = arr2.astype(np.int32)
print("After conversion nums are: ", arr3)
print("Datatype of After conversion nums is", arr3.dtype)