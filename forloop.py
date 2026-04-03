import numpy as np
arr = np.array([2,3,4,5,6,7])

for element in arr:
    print(element)
print("------------------------------------")

for i in arr:
    if(i%2 == 0):
        print(i)
print("------------------------------------")

arr1 = np.array(
    [
        [2,3],
        [5,6]
    ]
)
# when you need to print 2D array 
for i in arr1:
    for x in i:
        print(x)