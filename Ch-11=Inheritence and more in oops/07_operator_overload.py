class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(2)

print(n+m)

# for n-m __sub__
# for n*m __mul__
# for n/m __truediv__
# for n/m __floordv__