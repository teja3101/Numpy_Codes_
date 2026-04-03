import numpy as np
buffer_obj = b'\x01\x02\x03\x04\x05\x06'
arr = np.frombuffer(buffer_obj, dtype = np.uint8)
print(arr)