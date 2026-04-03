import numpy as np
a = np.array([1,2,3,5,6,7,8,10])    
new = np.argwhere(a > 3)           #it will return indices in 2D 
print(new)       
