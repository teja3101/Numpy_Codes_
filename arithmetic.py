import numpy as np
a = np.array([6,8,10])         
b = np.array([2,3,4]) 

# add()
print(np.add(a,b))

# subtract()
print(np.subtract(a,b))

# multiply()
print(np.multiply(a,b))

# divide()
print(np.divide(a,b))

# d = np.array([2.658,3.25,4.56]) 
# floor_divide()
# print(np.floor_divide(d))

# power()
print(np.power(a,b))

# mod()
print(np.mod(a,b))

# remainder()                   #same as modulus
print(np.remainder(a,b))

# reciprocal()                  #1/6, 1/8, 1/10 = [0,0,0]
print(np.reciprocal(a))


c = np.array([-5,-9,-72])
# negative()
print(np.negative(c))

# abs()
print(np.abs(c))