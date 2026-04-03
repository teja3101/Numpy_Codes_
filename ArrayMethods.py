import numpy as np
ar = np.array([1,2,3,4,5,6,7,78,8,9])
print(ar)

print(ar.reshape(2,5))
print(ar.sum())
print(ar.mean())
print(ar.max())
print(ar.min())

ar1 = np.array(
    [
        [1,4],
        [6,9]
    ]
)
print(ar1.max(axis=0))          #0 means with clms
print(ar1.min(axis=0))
print(ar1.max(axis=1))          #1 means with rows
print(ar1.min(axis=1))

print(ar.argmax())              #it showing max and min index number
print(ar.argmin())