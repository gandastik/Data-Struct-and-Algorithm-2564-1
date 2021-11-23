print("Enter Input : ", end='')
inp = [x.split() for x in input().split('/')]
a = [int(x) for x in inp[0]]
b = [int(x) for x in inp[1]]
a.sort()
for i in b:
    check = False
    for j in a:
        if(j > i):
            check = True
            print(j)
            break
    if(not check):
        print("No First Greater Value")