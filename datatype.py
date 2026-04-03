import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

arr1 = np.array([1,2,3,4], dtype = 'i')                                    #dtype = np.int16
print(arr1)

arr2 = np.array([1,2,3,4], dtype = 'f')                                    #dtype = np.float64
print(arr2)

arr3 = np.array([True,False,True], dtype = 'b')                            #dtype = np.bool_
print(arr3)

arr4 = np.array(["teju","chinu","priti"], dtype = np.str_)                 #fixed length str
print(arr4) 

# arr5 = np.array(["teju","chinu","priti"], dtype = np.chararray)          #flexible length str
# print(arr5)

# arr6 = np.array(['a','b','c'], dtype = np.character)
# print(arr6)

arr7 = np.array([1+2j, 2+3j, 5+6j], dtype = np.complex64)
print(arr7)

d1 = np.datetime64('2025-07-07')
d2 = np.datetime64('2025-07-05')
diff = d1 - d2
print(diff)
print(type(diff))

d3 = np.datetime64('2023-05-07 10:20:38')
print(d3)
print(type(d3))

o1 = np.array(["Teju", 21, 32.25,'a'], dtype = object)
print(o1)
print(type(o1))