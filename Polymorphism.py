# Dunder Functions __

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i + ", self.img,"j")


#here __add__ is a dunder function we can use + to add complex number using this function
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)



num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3  = num1 + num2 #this is not possible with python basic but can be done with dunder function
num3.showNumber()

num4 = num1 - num2
num4.showNumber()
