exp = [1,2,34,4]

for i in range(len(exp)):
    print(exp[i])
    
    
for i in exp:
    print(i)
    
print(" ")
for i, j in enumerate(exp):
    print(f"index: {i}, Value: {j}")
    
i=0
while i<10:
    i=i+1
    print(i)
