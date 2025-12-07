import numpy as np
import time
import sys


size = 1000000000000000000

list1 = range(size)
list2  = range(size)

np_array1 = np.array(size)
np_array2 = np.array(size)


#python array
start = time.time()
result = [(x+y) for x, y in zip(list1, list2)]
print("python list took:",(time.time()-size)*1000)

#numpy array
start = time.time()
result = np_array1 + np_array2
print("numpy took:",(time.time()-size)*1000)

