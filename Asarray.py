import numpy as np
import pandas as pd

s = pd.Series([1,3,5,6,8,7,9,767,67,6,5,69])
print(s)

data = [1,2,3,4,5,6,7]
tuple = (31,32,4,5,6,7,98,6,65)

ar = np.asarray(data)
print(ar)
ar1 = np.asarray(tuple)
print(ar1)

ar2 = np.asarray(s)
print(ar2)