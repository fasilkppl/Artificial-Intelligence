import numpy as np

a1 = np.array([1,0,1,2])
a2 = np.array([[1, 0], [1, 1], [1, 2]])


print(a2.ndim) #determines the dimension
print(a2.shape) #determines the shape [row, column]
print(a2.reshape(2,3))
print(a2.size) #determines the size(no. of elements)
print(a2.dtype) #determines the data type
print(a2.itemsize) #determines the size of each element
print(a2.itemsize*a2.size) #determines the size of the array 
print(a2.nbytes) #determines the size of the array in bytes
print(a2.ravel()) #flatens the array(makes any array to one dimension)
print(a2.max())
print(a2.min())
print(a2.sum(axis=0))
print(a2.sum(axis=1))
print("  ")


print(np.zeros((3,4)))
print("  ")
print(np.ones((3,4)))
print("  ")
print(np.linspace(1,5,10))
print("  ")
print(np.std(a2)) #standard deviation
print("  ")
print(np.sqrt(a2))




print("  ")
a3 = np.array([[1, 2], [3, 2], [5, 7]], dtype=np.complex128)
print(a3.itemsize) #determines the size
print(a3)


