#Recursive function to calculate the sum of first n natural numbers
def calc_sum(n):
    if(n == 0): #this is base condition
        return 0
    return calc_sum(n-1) + n #if sum(5) then sum(4)+ 5 .......

sum = calc_sum(10)
print(sum)


# Print all elements in a list

def el_list(list, idx=0):
    if(idx == len(list)): #setting base condition
        return
    print(list[idx])
    el_list(list, idx + 1 ) #it is updating its parameters so it is recursive function

fruits = ["apple", "banana", "cherry" , "mango"] #index starts from 0 and keeps increasing
# until the condition meets and return 

el_list(fruits)