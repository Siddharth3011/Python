class Empoyee:
    a = 1

    @property
    def name(self):
        return f"{self.fName} {self.lName}"
    
    @name.setter
    def name (self, value):
        self.fName = value.split(" ")[0]
        self.lName = value.split(" ")[1]

e = Empoyee()

e.name = "Siddharth Pandey"
print(e.fName , e.lName)
