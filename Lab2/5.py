print("*** TorKham HanSaa ***")
print("Enter Input : ", end="")
inputs = [str(x) for x in input().split(',')]
lst = []
curr = []
for i in inputs:
    lst.append(i.split(" "))

for i in lst:
    if(len(i) == 1):
        if(i[0] == 'R'):
            print("game restarted")
            curr = []
        elif(i[0] == 'X'):
            break
    #P mode
    else:
        if(i[0] == "P"):
            if(len(curr) != 0):
                lastTwoChar = curr[-1][-2:]
                #can be continue
                if(i[1][0].lower() == lastTwoChar[0].lower() and i[1][1].lower() == lastTwoChar[1].lower()):
                    #append the word to the list
                    curr.append(i[1])
                    print(f"'{i[1]}' -> [", end="")
                    for i in range(len(curr)):
                        if(i != len(curr) - 1):
                            print(f"'{curr[i]}', ", end="")
                        else:
                            print(f"'{curr[i]}']")
                #cannot be continue
                else:
                    print(f"'{i[1]}' -> game over")
                    break
            else:
                curr.append(i[1])
                print(f"'{i[1]}' -> ['{i[1]}']")
        elif(i[0] == "p"):
            print(f"'{i[0]} {i[1]}' is Invalid Input !!!")
            break
