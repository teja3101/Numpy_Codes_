import numpy as np
ar = np.array(['Tejaswini','chinya','Abhi','Prita'])       
new = np.char.replace(ar,'a','c',count=1)                   #each mdhil only one char will replace when count is set 
print(new)             