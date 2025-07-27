# Python Cheatsheet

This cheatsheet provides quick and clear explanations of commonly used Python concepts, including definitions and examples. Use this as a handy reference when working with Python.

## Table of Contents

1.  Variables
2.  Type Conversion
3.  Data Types
4.  Operators
5.  Statements
6.  List
7.  Range
8.  For Loops
9.  While Loops
10. Tuples
11. Functions & Built-in Functions
12. Recursion
13. File I/O
14. Class and Objects
15. Methods
16. Constructor
17. Class and Instance Attributes
18. Static Methods
19. Encapsulation
20. Abstraction

---

## 1. Variables

**Definition**: A variable is used to store data. It acts as a container for values in a program.

**Example**:
x = 10
name = "John"

In the above example:
x stores an integer 10
name stores a string "John"

## 2. Type Conversion

**Definition**:  Type conversion refers to converting one data type into another. In Python, this can be done using the int(), float(), and str() functions.

Example:
num_str = "15"
num_int = int(num_str)  # Converts string to integer
num_float = float(num_str)  # Converts string to float
Here:

"15" (a string) is converted to an integer 15 using int().

"15" is also converted to a float 15.0 using float().

## 3. Data Types

**Definition**: Data types define the type of a variable, such as numbers, strings, or more complex types.

Common Data Types in Python:
int: Integer, e.g., 5, -2

float: Floating-point number, e.g., 3.14, -7.8

str: String, e.g., "hello", 'Python'

list: Ordered collection of items, e.g., [1, 2, 3]

tuple: Immutable collection of items, e.g., (1, 2, 3)

bool: Boolean value, e.g., True, False

Example:
age = 25      # int
pi = 3.14     # float
name = "Alice"  # str
is_active = True  # bool

## 4. Operators

**Definition**: Operators are used to perform operations on variables and values. They can be arithmetic, comparison, logical, etc.

Types of Operators:
Arithmetic: +, -, *, /, %, //, **

Comparison: ==, !=, <, >, <=, >=

Logical: and, or, not

Example:
x = 10
y = 5
print(x + y)  # Addition: 15
print(x > y)  # Comparison: True


## 5. Statements

**Definition**: A statement is a unit of execution in Python, which may be an expression, an assignment, or a control flow statement.

Common Statements:
Assignment: Assigning values to variables

If-Else: Conditional execution of code blocks

Return: Returning a value from a function

Example:
if x > y:
    print("x is greater")
else:
    print("y is greater")

    
## 6. List

**Definition**: A list is a mutable, ordered collection of items, which can store values of different data types.

Example:
fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # Adds 'date' to the list
print(fruits)  # ['apple', 'banana', 'cherry', 'date']
Here, fruits is a list that contains four elements. You can add items to a list using append().

## 7. Range

**Definition**: The range() function generates a sequence of numbers. It is commonly used in loops to iterate over a sequence of numbers.

Example:
for i in range(5):
    print(i)
This will print the numbers from 0 to 4. You can specify a start and stop value in range(start, stop).

## 8. For Loops

**Definition**: A for loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code repeatedly.

Example:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
Here, the loop goes through each element in the fruits list and prints it.

## 9. While Loops

**Definition**: A while loop executes a block of code as long as a condition is True.

Example:

x = 0
while x < 5:
    print(x)
    x += 1  # Increment x
In this example:

The loop runs as long as x is less than 5.

After each iteration, x is incremented by 1.

## 10. Tuples

**Definition**: A tuple is an immutable (unchangeable) ordered collection of items. It is similar to a list, but once created, its values cannot be modified.

Example:

coordinates = (10, 20)
print(coordinates[0])  # 10
Here:
coordinates is a tuple containing two numbers.
You can access elements in a tuple using indexing, but you cannot modify them after creation.

## 11. Functions & Built-in Functions
**Definition**: A function is a block of reusable code that performs a specific task. Python also provides built-in functions like len(), sum(), print(), etc.

**Example**
def greet(name):
    return f"Hello, {name}!"

print(greet("Sandesh"))

Explanation:
The function greet takes one parameter name and returns a greeting message. print() is a built-in function.

## 12. Built-in functions

**Example**
numbers = [1, 2, 3, 4]
print(len(numbers))     # Returns 4
print(sum(numbers))     # Returns 10


Explanation:
len() gives number of elements, sum() gives the total.


## 13. Recursion

**Definition**: A function calling itself is known as recursion. Often used for tasks like factorial, Fibonacci, etc.

**Example 1: Factorial**
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

Explanation:
Each call reduces the problem by 1 until the base case (0) is reached.


**Example 2: Fibonacci**
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8

Explanation:
Calculates Fibonacci recursively. Avoid for large n without optimization.


## 14.  File I/O
**Definition**: Python uses open(), read(), write() to perform input/output operations on files.

**Example 1: Writing to a file**
with open("data.txt", "w") as file:
    file.write("Hello File!")
    
Explanation:
Creates (or overwrites) a file and writes a string.

**Example 2: Reading from a file**

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    
Explanation:
Reads all contents from data.txt.

## 15.Class and Objects
**Definition**: A class is a blueprint for creating objects. An object is an instance of a class.

**Example 1: Simple class**

class Car:
    def drive(self):
        print("Car is moving")

my_car = Car()
my_car.drive()

Explanation : Class Car has a method drive, which is called via object my_car.




**Example 2: Class with attributes**

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Sandesh")
print(s1.name)


Explanation : __init__() initializes object attributes when an object is created.


## 16.Methods

 **Definition**:Functions defined in a class are called methods.

**Example 1: Instance method**
class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
Explanation : bark is an instance method called using object d.


**Example 2: Method with arguments**

class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()
print(c.add(3, 5))  # 8

add takes two arguments and returns the sum.


**17.Constructor**
**Definition:** The __init__() method initializes a newly created object.

**Example 1: Constructor with one attribute**

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Sandesh")
print(p.name)

**Example 2: Constructor with multiple attributes**

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("Python", "Guido")
print(b.title, b.author)
Explanation:
Constructors assign values to object attributes during object creation.

**18.Class and Instance Attributes**
**Definition:** Instance attributes are specific to each object.

Class attributes are shared among all instances.

**Example 1: Instance attribute**

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("A")
s2 = Student("B")
print(s1.name, s2.name)

Explanation:
Each student has their own name.

**Example 2: Class attribute**

class School:
    school_name = "ABC School"

s1 = School()
s2 = School()
print(s1.school_name, s2.school_name)

Explanation:
Both objects share the same school_name.

**19.Static Methods**
**Definition:** @staticmethod defines a method that doesn’t access instance or class variables.

**Example 1: Static method**
class Math:
    @staticmethod
    def square(x):
        return x * x

print(Math.square(4))  # 16

**Example 2: Utility method**

class Utility:
    @staticmethod
    def greet():
        print("Welcome!")

Utility.greet()

**Explanation:**
Can be called without creating an object.

**20.Encapsulation**
**Definition:** Encapsulation hides the internal state of an object and restricts access.

**Example 1: Using private variable**

class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

a = Account()
a.deposit(100)
print(a.get_balance())  # 100
Explanation:
__balance is private; can’t be accessed directly.

**Example 2: Access via method**

class Employee:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

e = Employee("Sandesh")
print(e.get_name())

**.Abstraction**
**Definition:** Abstraction hides unnecessary implementation details and shows only essentials. Achieved using abstract classes or interfaces.

**Example 1: Abstract class (using abc)**

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
Explanation:
Can't create object of abstract class.

**Example 2: Implementing abstract class**

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())
Explanation:
Subclass must override area() or else it will error.













 

