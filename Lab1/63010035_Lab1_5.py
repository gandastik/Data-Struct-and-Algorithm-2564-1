n = int(input("Enter Input : "))
t = 6 + 2*(n-1)
for i in range(t):
    for j in range(t):
        #top left triangle
        if(i+j >= 2+(n-1) and i+j <= 4+2*(n-1) and j <= 2+(n-1) and i <= 2+(n-1)):
            print("#", end="")
        #bottom left triangle
        elif(i+j >= 6+2*(n-1) and i+j <= 8+3*(n-1) and i >= 3+(n-1) and j >= 3+(n-1)):
            print("+", end="")
        #top right rectangle
        elif(j >= 3+(n-1) and i<= 2+(n-1)):
            if(i < 2+(n-1) and i > 0 and j > 3+(n-1) and j < 5+2*(n-1)):
                print("#", end="")
            else: print("+", end="")
        #bottom right rectangle
        elif(j <= 2+(n-1) and i >= 3+(n-1)):
            if(i > 3+(n-1) and i < 5+2*(n-1) and j > 0 and j < 2+(n-1)):
                print("+", end="")
            else: print("#", end="")
        else:print('.', end="")
    print('')