from collections import deque

class Queue:

    def __init__(self, items = None):
        if(items == None):
            self.items = deque()
        else:
            self.items = deque(items, len(items))
        
    def enqueue(self, i):
        self.items.append(i)

    def dequeue(self):
        if(self.isEmpty()):
            return -1
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Stack:

    def __init__(self, items = None):
        if(items == None):
            self.items = []
        else:
            self.items = items
        
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        if(self.isEmpty()):
            return -1
        return self.items.pop(-1)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def checkTriplets(self, intercept = None):
        if(intercept == None):
            intercept = Queue()
        S = Stack([x for x in self.items])
        SS = Stack()
        crush = True
        curr = None 
        fcount = 0
        q = Queue()
        while(crush == True):
            count = 0
            for i in range(S.size()):
                x = S.pop()
                SS.push(x)
                if curr == x:
                    count += 1
                else:
                    curr = x
                    count = 1
                if count == 3:
                    if(intercept.isEmpty()):
                        count = 0
                        q.enqueue(curr)
                        for i in range(3):
                            SS.pop()
                    else:
                        ret = intercept.dequeue()
                        SS.items.insert(-1, ret)
                        if(SS.items[-1] == ret and SS.items[-3] == ret):
                            fcount += 1
                    crush = True
            crush = False
            count = 0
            for i in range(SS.size()):
                x = SS.pop()
                S.push(x)
                if curr == x:
                    count += 1
                else:
                    curr = x
                    count = 1
                if count == 3:
                    if(intercept.isEmpty()):
                        count = 0
                        q.enqueue(curr)
                        for i in range(3):
                            S.pop() 
                    else:
                        ret = intercept.dequeue()
                        S.items.insert(-1, ret)
                        if(S.items[-1] == ret and S.items[-3] == ret):
                            fcount += 1
                    crush = True
        return (q, S, fcount)
            


print("Enter Input (Normal, Mirror) : ", end='')
lst = [x for x in input().split()]
normalQ = Queue()
normalS = Stack()
mirrorQ = Queue()
mirrorS = Stack()
fcount = 0

for i in lst[0]:
    normalQ.enqueue(i)
for i in range(len(lst[0])-1, -1, -1):
    normalS.push(lst[0][i])
for i in lst[1]:
    mirrorS.push(i)

mirrorQ , mirrorS, fcount = mirrorS.checkTriplets()
tempQ = Queue([x for x in mirrorQ.items])
normalQ, normalS, fcount = normalS.checkTriplets(tempQ)

print("NORMAL : ")
if(normalS.size() == 0):
    print('0')
    print('Empty')
else:
    print(normalS.size())
    for i in normalS.items:
        print(f'{i}', end='')
    print('')
print(f'{normalQ.size() - fcount} Explosive(s) ! ! ! (NORMAL)')
if(fcount > 0):
    print(f'Failed Interrupted {fcount} Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
if(mirrorS.size() == 0):
    print('0')
    print("ytpmE")
else:
    print(mirrorS.size())
    for i in mirrorS.items:
        print(f'{i}',end='')
    print('')
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirrorQ.size()}')
# print(normalQ.items)
# print(mirrorQ.items)