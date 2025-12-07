total = 0
def sum(a,b):
    total = a+b
    print('total inside function: ', total)
    return total


abval = sum(b=2,a=10)
abval = sum(b=2,a=10)

print('total outside function: ', abval)
print('total variable outside the function: ',total) #scope of total ends outside the func, total=0 is global
