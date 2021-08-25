class Calculator :
    def __init__(self, val: int):
        self.val = val

    def __add__(self, n):
        return self.val + n.val

    def __sub__(self, n):
        return self.val - n.val

    def __mul__(self, n):
        return self.val * n.val

    def __truediv__(self, n):
        return self.val / n.val
        
x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))
print(x+y,x-y,x*y,x/y,sep = "\n")