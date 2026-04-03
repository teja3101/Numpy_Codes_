import numpy as np

s = np.array([1,3,5,6,8,7,9,767,67,6,5,69])
view = s[3:7]
print(view)

view[1] = 31                          #he view mdhe changes krel ani original arr print krel
print(s)