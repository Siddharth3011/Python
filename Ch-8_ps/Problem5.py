# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     print("*"*n, end="")
#     n -=1
#     print("")

# solve by using function: 

n = int(input("Enter the number: "))
def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)

pattern(n)

