def temp(fahrenheit):
    celcius = 5*(fahrenheit-32)/9
    return celcius

fahrenheit = int(input("Enter the temp in fahrenheit: "))
c = temp(fahrenheit)
print(f"{round (c,2)} degree celcius")