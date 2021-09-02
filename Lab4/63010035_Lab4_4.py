from collections import deque
class Queue:

    def __init__(self, items = None):
        if(items == None):
            self.items = deque()
        else:
            self.items = deque(items, len(items))
        self.act = ['Eat', 'Game', 'Learn', 'Movie']
        self.place = ['Res.', 'ClassR.', 'SuperM.', 'Home']
    
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

    def __str__(self):
        s = ''
        for i in range(len(self.items)):
            if(i != len(self.items) - 1):
                s += f'{self.items[i]}' + ', '
            else:
                s += f'{self.items[i]}'
        return s

    def getVerbose(self):
        s = ''
        for i in range(len(self.items)):
            s += self.act[int(self.items[i][0])] + ':'
            s += self.place[int(self.items[i][2])] 
            if(i != len(self.items) - 1):
                s += ', '
        return s

print("Enter Input : ",end='')
lst = [x.split() for x in input().split(',')]
myQueue = Queue()
yourQueue = Queue()
score = 0
for i in lst:
    myQueue.enqueue(i[0])
    yourQueue.enqueue(i[1])
    
print(f'My   Queue = {myQueue}')
print(f'Your Queue = {yourQueue}')
print(f'My   Activity:Location = {myQueue.getVerbose()}')
print(f'Your Activity:Location = {yourQueue.getVerbose()}')

while(not myQueue.isEmpty()):
    my = myQueue.dequeue()
    your = yourQueue.dequeue()
    #Same activity different place +1
    if(my[0] == your[0] and my[2] != your[2]):
        score += 1
    #Same place difference activity +2
    elif(my[0] != your[0] and my[2] == your[2]):
        score +=2
    elif(my[0] == your[0] and my[2] == your[2]):
        score += 4
    else:
        score -= 5

if(score >= 7):
    print(f"Yes! You're my love! : Score is {score}.")
elif(score >= 1):
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")
