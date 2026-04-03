import numpy as np
arr = np.array([1,2,3,4,5,6,6,2,6,4,3,5])

# Resize
ar1 = np.resize(arr,15)
print(ar1)

# Append
ar2 = np.append(arr,31)
print(ar2)

# Insert
ar3 = np.insert(arr,5,21)
print(ar3)

# Delete
ar4 = np.delete(arr,8)
print(ar4)

# Unique
ar5 = np.unique(arr)
print(ar5)