def selectionSort(num, n):
    if(n == 0):
        return
    else:
        max_ = findMax(num[:n], n)
        i = findIndex(num, len(num)-1, max_)
        inp[n-1], inp[i] = inp[i], inp[n-1]
        if(inp[n-1] != inp[i]):
            print(f'swap {inp[i]} <-> {inp[n-1]} : {inp}')
    selectionSort(num, n-1)

def findMax(num, n):
    if(n == 1):
        return num[0]
    return max(num[n-1], findMax(num, n-1))
    
def findIndex(num, n, item):
    if(n == 0):
        return 0
    if(item == num[n]):
        return n
    return findIndex(num, n-1, item)


print("Enter Input : ",end='')
inp = [int(x) for x in input().split()]
selectionSort(inp, len(inp))
print(inp)