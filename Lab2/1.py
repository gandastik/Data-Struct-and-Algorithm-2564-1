class Calculator :
    def __init__(self, val: int):
        self.val = val

    def __add__(self, a: int, b: int):
        return a + b

    def __sub__(self, a: int, b: int):
        return a-b

    def __mul__(self, a: int, b: int):
        return a*b

    def __truediv__(self, a: int, b: int):
        return a/b
        
x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))
print(x.__add__(x.val, y.val))
print(x.__sub__(x.val, y.val))
print(x.__mul__(x.val, y.val))
print(x.__truediv__(x.val, y.val))
