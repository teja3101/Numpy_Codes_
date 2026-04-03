import numpy as np 
ar1 = np.array([1,2,3,4,5,6,7,8])
# print(len(ar1))
sub_arr = np.split(ar1, 4)
print(sub_arr)
for i in sub_arr:
    # for j in i:
    #     print(j)
    print(i)