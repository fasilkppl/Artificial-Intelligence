food={}

#stored two key (juices, dishes) in an empty dictionary and assigned both the keys a new dictionary as a value.
food['juices'] = {'mango' : 8, 'apple' : 6, 'banana' : 10 }

food['dishes'] = {'porotta' : 2, 'idiyappam' : 4, 'puttu' : 5 }


def food_func(food_list):
    for item in food_list:
        print('key : ',item, "value : ",food_list[item])


food_func(food)

print(food['juices']['mango'])

