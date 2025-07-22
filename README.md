# Python Cheatsheet

This cheatsheet provides quick and clear explanations of commonly used Python concepts, including definitions and examples. Use this as a handy reference when working with Python.

## Table of Contents

1. [Variables](#variables)
2. [Type Conversion](#type-conversion)
3. [Data Types](#data-types)
4. [Operators](#operators)
5. [Statements](#statements)
6. [List](#list)
7. [Range](#range)
8. [For Loops](#for-loops)
9. [While Loops](#while-loops)
10. [Tuples](#tuples)

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

