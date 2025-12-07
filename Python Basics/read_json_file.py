with open(r"P:\AI Engineer\book.txt", "r") as r:
    content = r.read()
    
print(content)

#in simple read mode the data will be string
data = open(r"P:\AI Engineer\book.txt", "r")

info=data.read()
print(info)
print(type(info))

#in json the data will be dictionary
import json
book = json.loads(info)
print(book)
print(type(book))

print(book['tom'])
print(book['tom']['rocket'])


#to print all
for persons in book:
    print('Key: ',persons,'Values : ',book[persons])

