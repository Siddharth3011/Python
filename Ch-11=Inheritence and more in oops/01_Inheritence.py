class Employes:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class programmers:
#     company =  "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is: {self.salary}")

#     def showLanguage(self):
#         print(f"The name is: {self.name} and the language is: {self.language} language")

class programmer(Employes):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.Language} language")

a = Employes()
b = programmer()

print(a.company, b.company)
