class programmers:
    company = "Microsoft"
    def __init__(self, name, salary, location):
        self.name = name
        self.salary = salary
        self.location = location

p1 = programmers("sid",   1200000, "Ghaziabad")
p2 = programmers("Rohan", 1100000, "Ghaziabad")
p3 = programmers("Sohan", 1000000, "Ghaziabad")
print(p1.name, p1.salary, p1.location)       
print(p2.name, p2.salary, p2.location)       
print(p3.name, p3.salary, p3.location)       
