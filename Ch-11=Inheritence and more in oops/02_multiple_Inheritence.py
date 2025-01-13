class Employes:
    company = "ITC"
    name = "Sid"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class coder:
    language = "py"
    def oplanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

class programmer(Employes, coder):
    company = "ITC Infotech"
    name = "Sid"
    language = "py"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language} language")

a = Employes()
b = programmer()

print(a.company, b.company)
b.show()
b.oplanguage()
b.showLanguage()