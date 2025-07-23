#Recursive Function: When a function call itself again and again
#It is like a advanced loop

# 1

def show(n):
    if n== 0: #base case
        return
    print(n)
    show(n-1) # we cannot call this without any base case

show(10)

# 2
def fact(n):
    if(n == 0 or n == 1): #base condition factorial of 1 or 0 is 1
        return 1
    else:
        return n * fact(n-1)  #until the above condition is false we execute this

print(fact(6))