import numpy as np

# Rule - 1
a = np.array([1,2,3])
b = np.array([3,5,6])
r1 = a + b
print(r1)
print("---------------------------------")

# Rule - 2
c = np.array([1,2,3])
d = np.array(
    [
        [2,5,6],
        [6,4,7],
        [5,7,9],
        [7,4,9]
    ]
)
print(c + d)
print("---------------------------------")

# Rule - 3
e = np.array([1,2,3,4,5,6,7,8])
scalar = 5
r2 = e + scalar
print(r2)
