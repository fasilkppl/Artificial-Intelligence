#List Comprehensions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [i for i in numbers if i%2 == 0] 
print(even)

odd_squareRoot = [i*i for i in numbers if i%2 != 0]
print(odd_squareRoot)

#set Comprehension
#set removes all duplicates, no indexing
print(set([1, 2, 3, 4, 5, 6, 1, 2, 3]))

odd_squareRoot = {i*i for i in numbers if i%2 != 0}
print(odd_squareRoot)


#dictionary Comprehension
country = ['india', 'uae', 'usa', 'germany', 'antartica']
cities = ['kerala', 'dubai', 'new york','munich', 'ice berg']

merged = zip(country, cities) #merging two list

geographical_details = {country : cities for country, cities in merged}

print(geographical_details)