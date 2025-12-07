
#Multiple inheritence (two parents - one child)
class Animals:
    def furs(self):
        print("parent function")
class Mammals:
    def landLiving(self):
        print("parent function 2")


class Dog(Animals, Mammals):
    def behaviour(self):
        print("child function ")


obj = Dog()
obj.furs()
obj.landLiving()
obj.behaviour()

