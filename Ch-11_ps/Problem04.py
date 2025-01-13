class complex:
    def __init__(self, i,j):
        self.i = i
        self.j = j

    def __add__(self, c2):
        return complex(self.i + c2.i , self.j + c2.j)
    
    def __str__(self):
        return f"{self.i} + {self.j}i"
    
    def __mul__(self,c2):
        real_part = self.i * c2.i - self.j * c2.j
        imag_part = self.i * c2.j + self.j * c2.i
        return complex(real_part, imag_part) 
    
c1 = complex(1,2)
c2 = complex(3,4) 
print(c1 + c2)
print(c1 * c2)