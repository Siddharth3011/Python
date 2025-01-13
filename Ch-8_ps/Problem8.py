n = int(input("Enter the numeber you want to print its table: "))
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply(n)