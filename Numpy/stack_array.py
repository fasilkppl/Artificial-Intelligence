import numpy as np
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)



res = np.vstack((a,b))
print('a:',a)
print(" ")
print('b:',b)
print(" ")


print('vstack:',res)

res = np.hstack((a,b))

print(" ")

print('hstack:',res)
