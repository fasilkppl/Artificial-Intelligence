cars = {'lambo':636, 'volkswagen': 4747}

var=cars['lambo']
print(var)



#adding to dict

cars['bugatti'] = 35636

print(cars)

del cars['lambo']

print(cars)

for key in cars:
    print('Key: ',key,'value : ', cars[key])  #cars[key] is possible becoz data type is dict 
    
for i,j in cars.items():
    print('Key: ',i,'value : ', j)
    
    
print('bugatti' in cars)

n=cars.clear()
print(n)


#tuple
points = (2,4)
print(points[1])
