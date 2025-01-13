class Employee: 
    language = "py" #This is a class attribute
    salary = 1200000 

    def __init__(self, name, language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")
        

    def getinfo(self):
        print(f"your language is: {self.language}, and your salary is: {self.salary}")

    @staticmethod
    def greet():
        print("good morning")

siddharth = Employee("Siddharth", 120000, "js")
print(siddharth.name, siddharth.language, siddharth.salary)