import numpy as np
 
arr = np.arange(12).reshape(3,4)
print(arr)
print('flatten')
for i in np.nditer(arr,order='C'):
    print(i)

print(' fortan order')
for i in np.nditer(arr,order='F'):
    print(i)
print(' using flag - external loop')
for i in np.nditer(arr,order='F',flags=['external_loop']):
    print(i)

print(' using flag - read/write')
for i in np.nditer(arr,op_flags=['readwrite']):
    i[...]=i*i #returns square of arr
print(arr)