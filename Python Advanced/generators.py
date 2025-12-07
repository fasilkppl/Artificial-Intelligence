def remote_control_next ():
    yield "CNN"
    yield "ESPN"

generator_obj = remote_control_next()
print (generator_obj)

print(next(generator_obj))
print(next(generator_obj))



'''
That’s because when a function contains the yield keyword,
Python automatically turns it into a generator function.
'''