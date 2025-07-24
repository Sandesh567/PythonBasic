# FILE I/O in Python


# 1 accessing using open and passing file name and mode
# f  = open("demo.txt" ,"r")
# data = f.read() #reading the data
# print(data) #printing the data
# print(type(data)) #Printing the data types
# f.close() # Closing the operation



# 2 Reading only specific character

# f = open("demo.txt","r")
# data = f.read(5) #reading only 5 character from a file
# print(data)
# f.close()

# 3 Reading only one line at a time
f = open("demo.txt","r")
data = f.readline() #Print only the first line
print(data)
f.close()