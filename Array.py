import numpy 

ar = numpy.array([1,2,3,4,5,6,7,8,9,10])            #ar is the ndarray object
print(ar)

ar1 = numpy.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10]])           
print(ar1)

# access val by index number
print(ar1[0])
print(ar1[-1])
print(ar1[2][1])                      

# make element as like their data type
ar2 = numpy.array([1,2,3,4,5,6,7,8,9,10], dtype='f')           
print(ar2[0])

ar3 = numpy.array(['Teju','chinu','priti','aishu'], dtype=numpy.str_)
print(ar3)