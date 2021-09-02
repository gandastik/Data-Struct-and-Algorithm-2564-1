class Stack:

    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop(-1)
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

print(" ***Decimal to Binary use Stack***")
print("Enter decimal number : ", end='')
dec = int(input())
temp = dec
stack = Stack()
while(temp > 0):
    stack.push(temp % 2)
    temp = temp // 2

print("Binary number : ", end='')
while(not stack.isEmpty()):
    print(stack.pop(), end='')