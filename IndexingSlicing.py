import numpy as np
ar1 = np.array(
     [
         [1,2,6,7],
         [3,4,8,9]
     ]
)           
print(ar1[0][2])

ar2 = np.array(
     [
        1,2,34,6,7,8,9,9,2,3,5,6,6,7,5,4
     ]
)      
print(ar2[::])                #take all val from Array  
print(ar2[0:10])
print(ar2[4:9])
print(ar2[5:])