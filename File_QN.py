# # 1. Create a new file "practice.txt" and the text to it.

with open("practice.txt", "w") as f:
    f.write("Hi everyone \nwe are learning FILE I/O\n")
    f.write("using Java. \nI like programming in Java.")
    f.close()



# # 2. Replace java with python in practice.txt

with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)

with open("practice.txt" ,"w") as f:
    f.write(new_data)
#
#
# # 3. Search if learning word exists in the file called practice.txt
#
search = "nolearning"

with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(search) != -1):
        print("Found")
    else:
        print("Not Found")


# 4. check in which line programming is

def check_line():
    word ="programming"
    data = True
    line_no = 1
    with open("practice.txt" , "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_line())