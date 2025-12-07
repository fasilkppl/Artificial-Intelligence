import numpy as np
import sys
import time

#calculating the total memory consumption

#python array
list = range(1000) #list array
print(sys.getsizeof(1)*len(list))  #getting the size of list array in bytes


#numpy array
array = np.arange(1000)  #numpy array
print(array.size*array.itemsize) #getting the size of numpy  array in bytes