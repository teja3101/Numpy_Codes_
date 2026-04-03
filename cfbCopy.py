import numpy as np
a = np.array([1,2,3,5,6,7,8,10])  

# copy
b = a.copy()
print(b)
b[2] = 31
print(b)
print(a)
print("----------------------------------------")

# fancy indexing
indices = [2,6,3]
c = a[indices]
print(c)
c[1] = 31
print(c)
print(a)
print(b)
print("----------------------------------------")

# boolean indexing
condition = (a>=6)
d = a[condition]
print(d)
d[0] = 52
print(d)
print(a)
print(b)
print(c)

# updated array will come 