import numpy as np

arr = np.array([[1,2],[3,4],[5,6]],dtype=int)

#write

np.savetxt('numpy-file.txt',arr,fmt='%0.10g') # fmt='%0.10f' (float) , fmt='%0.10e' (scientific notation)

#read
arr_read = np.loadtxt('numpy-file.txt')

# Set print options

print(arr_read)