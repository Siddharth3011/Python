class Employee: 
    language = "py" #This is a class attribute
    salary = 1200000 

siddharth = Employee()
siddharth.name = "Siddharth" #This is a instance attribute
siddharth.language = "js"
print(siddharth.name, siddharth.salary, siddharth.language)

'''
here js printed because instance attributed takes more priority than class attributes.
'''