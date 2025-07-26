#Object Attribute has higher precedence than class attribute.
#Attribute simple means value

class Student:
    college_name = "KCMIT"
    name = "Unknown" #Class Attribute

    def __init__(self,name,marks):
        self.name = name #Object Attribute
        self.marks = marks
        print("Adding new students in database...")


s1 = Student("Sandesh",70)
print(s1.name,s1.marks)