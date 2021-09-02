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

print("Enter Input : ",end='')
lst = [x.split() for x in input().split(',')]
queue = Queue()
idx = 0
for i in lst:
    if(i[0] == 'E'):
        queue.enqueue(i[1])
        print(f'Add {i[1]} index is {idx}')
        idx += 1
    elif(i[0] == 'D'):
        ret = queue.dequeue()
        if(ret == -1):
            print('-1')
        else:
            print(f'Pop {ret} size in queue is {queue.size()}')
            idx -= 1

if(queue.isEmpty()):
    print("Empty")
else:
    print(f'Number in Queue is :  {list(queue.items)}')