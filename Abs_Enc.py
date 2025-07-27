#Abstraction means hiding the implementation details of a class
# and showing only the essential features to the user.
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.brk = True
        print("vrooom vrommmm !Car Started")

c1 = Car()

c1.start()

#Encapsulation - Wrapping data and function into a single unit(object)