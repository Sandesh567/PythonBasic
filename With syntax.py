# In with it will automatically close the file.


#Reading
with open("demo.txt" , "r") as f: #using alias
    data = f.read()
    print(data)


#Writing

with open("demo.txt", "w") as f:
    data = f.write("This is written!")


