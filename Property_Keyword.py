#Property - to use method as a property. helps in achieving the
#encapsulation concept and controlled access.

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

#whenever we use property then we will deal with the latest attribute and
    #change will be reflected.
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(98,89,99)
print(stu1.percentage)


#changing the marks and the attribute will be changed automatically
stu1.phy = 89
print(stu1.percentage)