import numpy as np
arr = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [8,9,5,6]
    ]
) 
flat_obj = arr.flat
for i in flat_obj:
    print(i)
