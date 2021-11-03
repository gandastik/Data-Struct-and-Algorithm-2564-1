def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

print('Enter Input : ',end='')
a, b = [int(x) for x in input().split()]
ret = gcd(a,b)
if(ret < 0):
    ret *= -1
if(a == 0 and b == 0):
    print("Error! must be not all zero.")
elif(a >= b):
    if(a < 0 and b < 0):
        print(f'The gcd of {b} and {a} is : {ret}')
    else:
        print(f'The gcd of {a} and {b} is : {ret}')
elif(b > a):
    print(f'The gcd of {b} and {a} is : {ret}')