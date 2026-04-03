import numpy as np
arr = np.array(
    [
        [2,4,8],
        [5,6,9]
    ]
)

for i, v in np.ndenumerate(arr):             #measure row wise
    print(i, v)
print("------------------------------------")