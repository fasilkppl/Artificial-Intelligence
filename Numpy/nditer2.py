import numpy as np

arr = np.arange(12).reshape(3,4)
print(arr)

print(' ')

brr = np.arange(3,15,4).reshape(3,1)
print(brr)

print(' ')

for i,j in np.nditer([arr,brr]):
    print(i,j)