#Create student class that takes name and marks of 3 subjects as arguments
#in constructor. Then create a method to print the average.

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name , "your average marks is:",sum / 3)


s1 = Student("sandesh",[87,88,90])
s1.avg_marks()


