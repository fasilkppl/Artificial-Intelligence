

class Human:
    #properties
    def __init__ (self,n,o):
        self.name = n
        self.occupation = o

    #methods
    def do_work(self):
        if self.occupation == 'tennis player':
            print("hi, im maria shavapora")
        elif self.occupation == 'actor':
            print("hi, im tom cruise")
            
    def speaks(self):
        print("I speak really well.")
    

tom = Human("Tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("Maria Shavapora" ,"tennis player")
maria.do_work()
maria.speaks()
