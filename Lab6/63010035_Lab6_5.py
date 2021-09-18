def asteroid_collision(asts):
    if(len(asts) == 0):
        return res
    if(res and asts[0] < 0 < res[-1]):
        if(res[-1] < -asts[0]):
            res.pop()
            asteroid_collision(asts)
            return
        elif(res[-1] == -asts[0]):
            res.pop()
            asteroid_collision(asts[1:])
            return
        elif(res[-1] > -asts[0]):
            asteroid_collision(asts[1:])
            return
    else:
        res.append(asts[0])
    asteroid_collision(asts[1:])
    
x = input("Enter Input : ").split(",")
x = list(map(int,x))
res = []
asteroid_collision(x)
print(res)