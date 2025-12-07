#List of Lists
test = [['march', 310.0],
 ['april', 340.0],
 ['may', 380.0],
 ['june', 302.0],
 ['july', 297.0],
 ['august', 323.0]]

#empty dict
cars = { }

#using a for loop, i added every element to a dict
for element in test:
    day = element[0]
    price = element[1]
    cars[day] = price #adding elements
print(cars)

print(cars['march'])