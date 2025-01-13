class Employee: 
    language = "py" #This is a class attribute
    salary = 1200000 

siddharth = Employee()
siddharth.name = "Siddharth" #This is a instance attribute
print(siddharth.name, siddharth.salary, siddharth.language)

rohan = Employee()
rohan.name = "Rohan" #This is a instance attribute
print(rohan.name, rohan.salary, rohan.language)

'''
Here name is a instance attribute and language and salary is a class attribute because they drectly belong to class.
'''