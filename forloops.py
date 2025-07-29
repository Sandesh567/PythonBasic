numbers = [1,2,3,4,5,6,7,8,9,10]

for item in numbers:
    print(item)


#Print each fruit in a fruit list

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Looping Through a String
for x in "banana":
  print(x)

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

    #With the break statement we can stop the loop before it has looped through all the items


#Exit the loop when x is "banana", but this time the break comes before the print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
