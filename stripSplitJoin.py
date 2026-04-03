import numpy as np
ar = np.array(['Tejaswini','     chinya    '])
# Strip()
print(np.char.strip(ar))
# Split()
print(np.char.split(ar,'i'))
# Join()
print(np.char.join('-',ar))