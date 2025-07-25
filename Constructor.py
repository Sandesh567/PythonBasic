#__init__() is a function that is called automatically even we do not write

class Student:
    # This is a constructor if we do not create it python will automatically create it for us.
     def __init__(self,name,marks):#always write self that's mandatary
         # storing the new value here:
         self.name = name
         self.marks = marks
         print("Adding new student in database...")


s1 = Student("Sandesh",70)
print(s1.name, s1.marks)
