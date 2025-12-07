class RemoteControl:
    def __init__(self, channels):
        self.channels = channels
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if len(self.channels) == self.index:
            raise StopIteration("list ended")
        return self.channels[self.index]

    def __reversed__(self):
        for channel in reversed(self.channels):
            yield channel

obj = RemoteControl(['CNN News, Pogo, Sonyliv, Asianet'])
itr = iter(obj)
print(next(itr))

itr = reversed(obj)
print(next(itr))


'''

When we define __iter__, __next__, or __reversed__ in our own class,
we are telling Python how those existing built-in functions should behave for our object.

So yes — we’re customizing the behavior of already existing built-in mechanisms,
but not modifying the built-ins themselves.

We’re just teaching Python what they mean for our specific class.


'''