cars = {'bugatti', 'pagani', 'lambo', 'rolls royce'}
cars.add('alfa romeo')
print(cars)

'''
Sets are unordered collections

Unlike lists, sets do not maintain any order of elements.

When you print a set, Python shows the elements in an arbitrary order.

Adding elements doesn’t guarantee position
 so we get shuffled elements as output each time running this.
'''

numbs = frozenset({1,2,3,4,5})
#numbs.add(7) this is not possible, we cannot mutate forzen 

words = {"flower", "success", "option", "game of thrones"}

print("success" in words)

#sets can be iterated
for i in words:
    print(i)
    

#union
x = {1,2,3,4,5}
y = {3,4,5,6,7}
print('Union: ', x|y) #each element one time

#intersection
print("Intersection : ",x&y) #common elements

print("Difference : ", x-y) #gives elements in x but not in y.

#subset
x = {'a','b','c','d','e'}
y = {'b', 'c', 'e'}

print(x>y) #all elements of y are in x, so y is a subset of x