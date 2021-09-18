def power(a, b):
    if(b == 1):
        return a
    elif(b == 0):
        return 1
    else:
        return a * power(a, b-1)

print("Enter Input a b : ", end='')
num = [int(x) for x in input().split()]
print(power(num[0], num[1]))
