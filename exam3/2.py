def findMax(n, lst):
    if(n == 0):
        return lst[0]
    return max(lst[n], findMax(n-1, lst))

print("Enter Input : ", end='')
inp = [int(x) for x in input().split()]
print(f'Max : {findMax(len(inp)-1, inp)}')