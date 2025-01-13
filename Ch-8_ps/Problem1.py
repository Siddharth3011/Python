def greatest():
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    num3 = int(input("Enter the number: "))

    if(num1>num2 and num1>num3):
        print("Num 1 is the gretest number")
    
    elif(num2>num1 and num2>num3):
        print("Num 2 is the gretest number")
    
    else:
        print("Num 3 is the gretest number")
    
greatest()