def get(num):
    if(len(num) == 1):
        return num[0]
    return get(num[:-1])
    
def sorting(num, n):
    if(n == 1):
        return
    else:
        x = get(num[len(num)-n:])
        y = get(num[len(num)-n+1:])
        if(x > y):
            num[len(num)-n], num[len(num)-n+1] = num[len(num)-n+1], num[len(num)-n]
    sorting(num, n-1)

def bubbleSort(num, n):
    if(n == 1):
        return
    else:
        sorting(num, len(num))
    bubbleSort(num, n-1)

print("Enter Input : ",end='')
inp = [int(x) for x in input().split()]
bubbleSort(inp, len(inp))
print(inp)