import numpy as np
arr = np.array(
    [
        [2,4],
        [5,6]
    ]
)

for element in np.nditer(arr, order = 'C'):             #measure row wise
    print(element)
print("------------------------------------")

for element in np.nditer(arr, order = 'F'):             #measure clm wise
    print(element)
print("------------------------------------")

for i in np.nditer(arr, order = 'F'): 
    if(i%2 == 0):
        print(i)