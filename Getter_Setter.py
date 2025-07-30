#Getter is a method used to access a private attribute
#Setter is a method ued to update or modify the private attribute

#@property is used to use getter and setter
#Ex. 1
class Product:
    def __init__(self,price):
        self.__price = price #private

    @property
    def price(self): #getter
        return self.__price

    @price.setter #getter function name .setter . this will define what happens when you add new value
    def price(self,value):  #setter function
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative")



p = Product(100)
print(p.price) #getter value access
p.price = 150 #updating with setter
print(p.price) #price will be 150

#Ex.2

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # private attribute

    @property
    def balance(self):  # Getter
        return self.__balance

    @balance.setter
    def balance(self, amount):  # Setter
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

# Using the class
acc = BankAccount("Sandesh", 1000)
print(f"Initial Balance: Rs. {acc.balance}")  # Using getter

acc.balance = 1500   # Using setter to update balance
print(f"Updated Balance: Rs. {acc.balance}")

acc.balance = -500   # Attempt to set negative balance
print(f"Final Balance: Rs. {acc.balance}")




