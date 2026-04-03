import numpy as np
a = np.array([1,2,3,5,6,7,8,10])  
mask = (a>3)  
print(a[mask])
print(a[a<6])
