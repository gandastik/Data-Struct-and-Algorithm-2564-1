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

def postFixeval(string):
    stack = Stack()
    for i in string:
        #check if i is a number (could be negative too)
        if(i.isnumeric() or (len(i) > 1 and i[0] == '-')):
            stack.push(float(i))
        else:
            if(i == '+'):
                b = stack.pop()
                a = stack.pop()
                stack.push(a + b)
            elif(i == '-'):
                b = stack.pop()
                a = stack.pop()
                stack.push(a - b)
            elif(i == '*'):
                b = stack.pop()
                a = stack.pop()
                stack.push(a * b)
            elif(i == '/'):
                b = stack.pop()
                a = stack.pop()
                stack.push(a / b)
    return stack.pop()

print(" ***Postfix expression calcuation***")
print("Enter Postfix expression : ", end='')
lst = [x for x in input().split()]
print(f'Answer :  {postFixeval(lst):.2f}')