import math
def Range(a = 0, b = 0, c = 1):
    ret = []
    #a = end when no other argument pass in , 
    if(b == 0 and c == 1):
        for i in range(math.ceil(a)):
            ret.append(float(i))
    elif(b != 0 and c == 1):
        n = math.ceil(b-a)
        for i in range(n):
            ret.append(a+i)
    else:
        n = math.ceil((b - a)/c)
        temp = a
        for i in range(n):
            #check for 1.0, 2.0 then append
            if(abs(int(temp) - temp) <= 0.00000001):
                ret.append(f'{temp:0.1f}')
            else:ret.append(f'{temp:g}')
            temp+=c
    return ret

#input prompt
print("*** New Range ***")
print("Enter Input : ", end="")
lst = [float(x) for x in input().split()]
ans = []

if(len(lst) == 1):
    ans = Range(lst[0])
elif(len(lst) == 2):
    ans = Range(lst[0], lst[1])
elif(len(lst) == 3):
    ans = Range(lst[0], lst[1], lst[2])

#answer format:
print("(",end='')
for i in range(len(ans)):
    if(i != len(ans)-1):
        print(f"{ans[i]}, ", end="")
    else:
        print(f"{ans[i]}",end="")
print(")")