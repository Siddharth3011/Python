class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of the number is: {self.n*self.n}")
        
    def cube(self):
        print(f"The cube of the number is: {self.n*self.n*self.n}")
        
    def square_root(self):
        print(f"The square root of the number is: {self.n**(1/2)}")

    @staticmethod
    def greet():
        print("hello there!")

a = calculator(16)
a.greet()
a.square()
a.cube()
a.square_root()