from collections import deque

class Queue:

    def __init__(self, items = None):
        if(items == None):
            self.items = deque()
        else:
            self.items = deque(items)

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        if(self.isEmpty()):
            return -1
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        if(self.isEmpty()):
            return "Empty Queue"
        s = 'Queue data : '
        for i in self.items:
            s += str(i) + ' '
        return s

    def __len__(self):
        return len(self.items)

    def checkForDup(self):
        for i in self.items:
            if(self.items.count(i) > 1):
                return "Duplicate"
        return "NO Duplicate"

print("Enter Input : ",end='')
lst = [str(x) for x in input().split('/')]
enQueueLst = [int(x) for x in lst[0].split()]
q = Queue(enQueueLst)
commandLst = [str(x) for x in lst[1].split(',')]
for i in commandLst:
    if(i[0] == 'E'):
        q.enQueue(int(i[2:]))
    elif(i[0] == 'D'):
        q.deQueue()
print(q.checkForDup())