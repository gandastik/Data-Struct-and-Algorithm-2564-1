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

print("Enter code,hint : ",end='')
string = str(input())
s = ord(string[-1]) - ord(string[0])
q = Queue()
for i in string:
    ch = chr(ord(i) + s)
    if(i == ','):
        break
    q.enqueue(ch) 

ret = []
while(not q.isEmpty()):
    ret.append(q.dequeue())
    print(ret)


