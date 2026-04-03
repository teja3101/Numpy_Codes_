import numpy as np
a = np.array([1,2,3,5,6,7,8,10])    
new = np.extract(a>3,a)
print(new)       
