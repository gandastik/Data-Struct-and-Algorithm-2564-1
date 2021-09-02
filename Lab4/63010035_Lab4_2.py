from collections import deque

class Queue:

    def __init__(self, items = None):
        if(items == None):
            self.items = deque()
        else:
            self.items = deque(items, len(items))
        self.s_items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def enqueueS(self, item):
        self.s_items.append(item)

    def dequeue(self):
        if(self.isEmpty() and len(self.s_items) == 0):
            return -1
        elif(len(self.s_items) != 0):
            return self.s_items.popleft()
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

print("Enter Input : ",end='')
lst = [x.split() for x in input().split(',')]
q = Queue()
for i in lst:
    if(i[0] == 'EN'):
        q.enqueue(i[1])
    elif(i[0] == 'D'):
        ret = q.dequeue()
        if(ret == -1):
            print("Empty")
        else:
            print(ret)
    elif(i[0] == 'ES'):
        q.enqueueS(i[1])
