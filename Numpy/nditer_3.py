

import numpy as np
arr = np.arange(15).reshape(3,5)
for i in np.nditer(arr,op_flags=['readwrite']):
    i[...]=i*i
print(arr)