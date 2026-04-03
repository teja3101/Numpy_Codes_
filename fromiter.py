import numpy as np
list = [1,2,3,4,5,6,7,8]
dict = {
    1:'Teju',
    2:'Chinu'
}
arr = np.fromiter(list, dtype = int)
print(arr)
print(type(arr))
arr1 = np.fromiter(dict, dtype = int)
print(arr1)
print(type(arr1))
# find max len str len to avoid truncation
max_len = max(len(s) for s in dict.values())
# use fromiter with dtype='U' + max_len
arr2 = np.fromiter(dict.values(), dtype = f'U{max_len}')
print(arr2)
print(type(arr2))
