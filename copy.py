import numpy as np
a = np.array([1,2,3,5,6,7,8,10])  
b = a.copy()
b[2] = 31
print(b)
print(a)