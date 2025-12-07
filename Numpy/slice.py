import numpy as np

arr = np.array([[1,2],[3,4],[5,6],[4,9]])

print(arr[:])
print(" ")
print(arr[0:2,1]) #row/column - [1,2] and [3,4] (row)/ [2,4](column)

print(arr[0:-1,1]) #row/column -[1,2][3,4][5,6] (row)/ [2 4 6](column)

print(arr[3,1:2])

print(arr[1:3,:])
