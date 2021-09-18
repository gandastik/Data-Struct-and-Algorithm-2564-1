def sorting(lst, n):
    if(n == 1):
        return
    else:
        x = traversal(lst[len(lst)-n:])
        y = traversal(lst[len(lst)-n+1:])
        if(x < y):
            lst[len(lst)-n] , lst[len(lst)-n+1] = lst[len(lst)-n+1], lst[len(lst)-n] 
    sorting(lst, n-1)

def traversal(lst):
    if(len(lst) == 1):
        return lst[0]
    return traversal(lst[:-1])

def sort(lst, n):
    if(n == 1):
        return
    else:
        sorting(lst, len(lst))
    sort(lst, n-1)

print("Enter your List : ", end='')
lst = [int(x) for x in input().split(',')]
sort(lst, len(lst))
print(f'List after Sorted : {lst}')