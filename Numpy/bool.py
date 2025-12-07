import numpy as np

arr = np.arange(12).reshape(3,4)

print(arr)

print(' ')
b = arr>5
arr[b] #here the index of the array is array itself. returns  the actual values for the true values(arr>5) in the  array
print(b)


print(' ')
print(arr[b])


print(' ')
arr[b]=-1 #sets all values greater than 5 to -1
print(arr)
print(b.dtype)