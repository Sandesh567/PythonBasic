# def is a keyword to define function def function_name(para1, para2):
#     some work
#         return value

# 1

def calc_sum(a,b):
    sum =  a + b
    print(sum)
    return sum

calc_sum(10,20)


# # 2

def addition(a,b):
    return a+b

total  = addition(10,30)
print(total)

# # 3

def average_marks(math,science, social):
    sum = math + science + social
    avg = sum / 3
    print("Your average marks is: "+ str(avg))
    return avg

average_marks(90,80,80)

# 4 - Calculate the length of the cities

cities = ["Ktm", "Pokhara","Chitwan","Dhangadhi" , "Dang","Rasuwa"]
names = ["Sandesh" ,"Anuj","Avishek" ,"Binit","Ashma"]

def len_city(cities, names):
    city_length = len(cities)
    name_length = len(names)
    print(city_length)
    print(name_length)

len_city(cities,names)

# 5 printing elements of a list in a single line

names = ["Sandesh" ,"Anuj","Avishek" ,"Binit","Ashma"]

def list_el(list):
    for item in list:
        print(item, end=" ")

list_el(names)

# 6 finding the factorial of n , n is the parameter

def calc_facto(n):
    fact = 1
    for i in range(1,n+1):  #from 1 to n
        fact *= i # current value is multilied in each iteration
    print(fact)

calc_facto(5)


# 7 - convert usd to npr 1usd = 137.63

def converter (usd_rate):
    npr_rate = usd_rate * 137.63
    print(usd_rate,"USD =" , npr_rate , "NPR")

converter(10)
