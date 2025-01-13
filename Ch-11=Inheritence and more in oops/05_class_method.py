class Empoyee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Empoyee()
e.a = 45

e.show()