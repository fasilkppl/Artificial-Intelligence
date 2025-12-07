def fibanocci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b  #We calculate a + b and store it in b, update a to the old b, and then yield the new a.
for f in fibanocci():
    if f > 50: #i need fibanocci of up to 50 - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
        break
    print(f) # this is yield a value
    
    
'''
yield is what makes this a generator.

Instead of returning a value and stopping, yield produces a value and pauses the function.

Next time the generator is called, it resumes where it left off.

Here, it yields the current Fibonacci number (a).
'''