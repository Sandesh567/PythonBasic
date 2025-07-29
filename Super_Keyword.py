#Super keyword is used to access the methods of the parent class

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Starting")

    @staticmethod
    def stop():
        print("Stopping")

class Toyota(Car):
    def __init__(self,name,type):
        super().__init__(type) #accesing the constructor of parent class
        self.name = name
        super().start() #accesing the start method from the parent class

car1 = Toyota("Fortuner","electric")
print(car1.type)