class Stack:
    def __init__(self, items = None):
        if(items == None):
            self.items = []
        else:
            self.items = items

    def push(self, i):
        self.items.append(i)

    def pop(self):
        self.items.pop(-1)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def bottom(self):
        return self.items[0]

    def __str__(self):
        s = 'Data in Stack is : '
        for i in self.items:
            s += str(i) + ' '
        return s


n = int(input("Enter choice : "))
if(n == 1): 
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
elif(n == 2):
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
elif(n == 3):
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())