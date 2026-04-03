import numpy as np
arr = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [8,9,5,6]
    ]
) 
print(arr)
new_arr = arr.ravel()
new_arr[0] = 31
print(new_arr)
print(arr)                       #ekda ka reval mdhe change jhal ki te affect krn original arr vr pn ani te hi change hot