

class Accident(Exception): #user defined exception is inherited from built in Exception class
    def __init__(self, message):
        self.message = message

    def userException(self):
        print("user defined exception invoked : ", self.message)


try:
    raise Accident ('Cars Crased Damn...Abort...')
except Accident as a: #user defined
    a.userException()
except ZeroDivisionError as z: #built in
    print("no use dawg")
finally:
    print("this block will execute no matter what")