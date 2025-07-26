#Methods are functions that belongs to objects

#Creating Class

#Constructor
class Student:
    def __init__(self,fullname,marks):
        self.fullname = fullname
        self.marks = marks


#Methods
    def hello(self): #Always write Self even we are not using it.
        print("Hello", self.fullname)

    def get_marks(self):
        return self.marks

#Creating Objects

s1 = Student("Sandesh",80)
s1.hello()
print(s1.get_marks())