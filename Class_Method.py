class Person:
    name = "Unknown"

    # def change(self,name):
    #     Person.name = name #indirect methods

    # def change(self,name):
    #     self.__class__.name = "Marshall"

    #using the class method
    #This will change the class attribute
    @classmethod
    def change(cls,name):
        cls.name = name



p1 = Person()
p1.change("Sandesh") #This will change the name inside the function
# won't change the class attribute
print(p1.name)
print(Person.name)

