class GameTorKham:
    def __init__(self, inputs):
        self.inputs = inputs
        self.lst = []
        self.curr = []

    def play(self):
        for i in self.inputs:
            self.lst.append(i.split(" "))

        for i in self.lst:
            if(len(i) == 1):
                if(i[0] == 'R'):
                    print("game restarted")
                    self.curr = []
                elif(i[0] == 'X'):
                    break
            #P mode
            else:
                if(i[0] == "P"):
                    if(len(self.curr) != 0):
                        lastTwoChar = self.curr[-1][-2:]
                        #can be continue
                        if(i[1][0].lower() == lastTwoChar[0].lower() and i[1][1].lower() == lastTwoChar[1].lower()):
                            #append the word to the list
                            self.curr.append(i[1])
                            print(f"'{i[1]}' -> [", end="")
                            for i in range(len(self.curr)):
                                if(i != len(self.curr) - 1):
                                    print(f"'{self.curr[i]}', ", end="")
                                else:
                                    print(f"'{self.curr[i]}']")
                        #cannot be continue
                        else:
                            print(f"'{i[1]}' -> game over")
                            break
                    else:
                        self.curr.append(i[1])
                        print(f"'{i[1]}' -> ['{i[1]}']")
                elif(i[0] == "p"):
                    print(f"'{i[0]} {i[1]}' is Invalid Input !!!")
                    break

print("*** TorKham HanSaa ***")
print("Enter Input : ", end="")
inputs = [str(x) for x in input().split(',')]
x = GameTorKham(inputs)
x.play()