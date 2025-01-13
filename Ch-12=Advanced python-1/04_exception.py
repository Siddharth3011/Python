try:
    a = int(input("Enter the number: "))
    print(a)

except ValueError as v:
    print("Hey")
    print(v)

except Exception as e:
    print(e)

print("Thamk you")