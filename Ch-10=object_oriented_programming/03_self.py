class Employee: 
    language = "py" #This is a class attribute
    salary = 1200000 

    def getinfo(self):
        print(f"your language is: {self.language}, and your salary is: {self.salary}")

    # def greet(self):
    #     print("good morning")
    # you can also write it as:

    @staticmethod
    def greet():
        print("good morning")

siddharth = Employee()
siddharth.greet()
siddharth.getinfo()