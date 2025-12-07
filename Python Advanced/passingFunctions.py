#Passing a function as an argument
def greet(name):
    return f"Hello, {name}!"

def call_func(func, value):
    return func(value)

result = call_func(greet, "Alice") #first i will go to call_func, then greet and then print results
print(result)


'''
In Python, functions are first-class objects, meaning you can:

Pass them as arguments to other functions

Return them from functions

Store them in variables, lists, or dictionaries
'''

#Returning a function from another function
def outer():
    def inner():
        return "Im the inner function!"
    return inner  # returns the function inner function     def inner(): return "Im the inner function!", not its result

my_func = outer()
print(my_func())  # now call the returned inner() function


'''
I’m the inner function!
Here, outer() returns a function — not a value — which we can later call.

'''
