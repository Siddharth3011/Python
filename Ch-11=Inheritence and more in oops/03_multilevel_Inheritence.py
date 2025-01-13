class Employee:
    language = "py"
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)

p = Programmer()
print(p.a)
print(p.b)

q = Manager()
print(q.a)
print(q.b)
print(q.c)

