class complex:
    def __init__(self, i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self, c2):
        return complex(self.i + c2.i , self.j + c2.j, self.k + c2.k)
    
    def __str__(self):
        return f"{self.i}i + {self.j}j +{self.k}k"
    
c2 = complex(7,8,10) 
print(c2)