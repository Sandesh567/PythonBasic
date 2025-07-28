# #Private attributes and methods are meant to be used only accessible
# #inside class and cannot be accessed outside the class
# # __ double hyphen is used to declare private


# #Private 1.
class Account:
    def __init__(self,acc_num, acc_pass):
        self.acc_num = acc_num
        self.__acc_pass = acc_pass  #private variable


account = Account(12345,"PASSWORD")
print(account.acc_num)  # not private can be accessed
print(account.__acc_pass)  #private so cannot be accessed in a subclass



# #Private 2.

class Person:
    __name = "Anonymous"

    def __hello(self):
        print("Hey i am : "+ self.__name) #internally accessing the value

    def welcome(self):
        self.__hello() #calling the methods internally


p1 = Person()
print(p1.welcome()) # then here we can print the value






# #Protected _ can be used in subclass and internal use
#
class Account:
    def __init__(self,acc_num, acc_pass):
        self.acc_num = acc_num
        self._acc_pass = acc_pass  #protected variable _



account = Account(12345,"PASSWORD")
print(account.acc_num)  # not private can be accessed
print(account._acc_pass)  #protected so can be accessed


