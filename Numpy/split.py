import numpy as np

arr = np.arange(30).reshape(2,15)
print(arr)

print(' ')
result = np.hsplit(arr,3)

print(result[0])
print(' ')
print(result[1])
print(' ')
print(result[2])
print(' ')


result = np.vsplit(arr,2)
print(result[0])
print(' ')
print(result[1])
print(' ')

