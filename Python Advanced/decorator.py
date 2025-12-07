import time
def time_it(func): #func refers to whichever function is being decorated,(calc_cube and calc_square) — like an alias or handle for that function.
    def wrapper(*args, **kwargs):
        start = time.time() #Records the start time
        result = func(*args,**kwargs) #Runs the original function (calc_cube and calc_square) (The *args and **kwargs mean it can handle any function arguments, no matter how many.)
        end = time.time() #Records the end time
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec") #Prints how long it took.
        return result #return the value of original function.
    return wrapper #returning wrapper from outside function.



@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)