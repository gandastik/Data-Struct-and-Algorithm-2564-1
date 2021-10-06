import math
class MyInt:
    def __init__(self, n):
        self.num = n

    def toRoman(self):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        num = self.num
        while(num > 0):
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i+=1
        pre = f'{self.num} convert to Roman : '
        return pre + roman_num

    def __add__(self, n):
        oldNum1 = self.num
        oldNum2 = n.num
        self.num += oldNum2/2
        n.num += oldNum1/2
        s = f'{oldNum1} + {oldNum2} = {int(self.num + n.num)}'
        return s

print(" *** class MyInt ***")
print("Enter 2 number : ", end='')
x, y = [int(x) for x in input().split()]
a = MyInt(x)
b = MyInt(y)
print(a.toRoman())
print(b.toRoman())
print(a+b)