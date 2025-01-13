try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    print(f"the divison of a/b is: {a/b}")

except ZeroDivisionError as v:
    print("we do not take value zero as a denominator")