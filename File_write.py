#Writing into a file

# 1 . Writing into the file means overwriting using "w".

f = open("demo.txt", "w")

f.write("This is new line added to the file.") #This overwrites the whole file

f.close()

# 2. If we want to add to the end of the file we use append "a"

f = open("demo.txt", "a") #This will add at the end of the file

f.write("\nThis text is written using the append operation")

f.close()


# 3. If there exist no file that we are creating then python will create that
#file for us. W and A does this.

f = open("sample.txt" ,"w")
f.write("This is a new file.")
f.close()

# 4. r+ this overwrites the beginning of the file. No truncate

f  = open("demo.txt" ,"r+")  #This will overwrite at the beginning of the file
f.write("hello!")
f.close()

# 5. w+ truncated the whole file

f = open("demo.txt" , "w+") # Removes everything and then write
f.write("clear")
f.close()

# 6. a+ no truncate last pointer