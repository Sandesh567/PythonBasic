#Inheritance _ when one class derives the property from another class
#It allows child or subclass to derive attribute methods from an existing class
#parent class or superclass.

#1. Single Level Inheritance

#Parent class
class Car:
    color = "red"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car Stopped..")


# child class

#We are inheriting the whole car class and all its methods can be accessed
class Toyota(Car):
      def __init__(self,name):
          self.name = name


# Object creation
car1 = Toyota("Fortunar")
car2 = Toyota("Prius")

print(car1.name) #we can do this and print car name

print(car1.start()) # we can do this and access the methods from car class

print(car2.color)


# 2. Multi Level Inheritance

class Gadi():

    @staticmethod
    def start1():
        print("Car started vroom......")

    @staticmethod
    def stop1():
        print("Car Stopped disssssss..")


class Mercedes(Gadi):
    def __init__(self,name):
        self.name = name


class Type(Mercedes):
    def __init__(self,type):
        self.type = type


gadi = Mercedes("Benz")
gadi.start1()


#Multiple inheritance

class A:
    varA  = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


