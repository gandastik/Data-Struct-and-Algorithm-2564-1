class Stack:
    
    def __init__(self, items = None):
        if(items == None):
            self.items = []
        else:
            self.items = items
        
    def push(self, i):
        self.items.append(i)
        
    def pop(self):
        return self.items.pop(-1)

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def lookBack(self):
        if(self.isEmpty()):
            return 0
        temp = Stack([x for x in self.items])
        tallest = temp.pop()
        count = 1
        while(not temp.isEmpty()):
            new = temp.pop()
            if(new > tallest):
                tallest = new
                count += 1
        return count

print("Enter Input : ", end='')
lst = [x.split() for x in input().split(',')]
stack = Stack()
for i in lst:
    if(i[0] == 'A'):
        stack.push(int(i[1]))
    elif(i[0] == 'B'):
        print(stack.lookBack())