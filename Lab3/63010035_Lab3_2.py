class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if(len(self.items) == 0):
            return - 1
        return self.items.pop(-1)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def delete(self, i):
        if(len(self.items) == 0):
            return -1
        count = 0
        while(1):
            try:
                self.items.remove(i)
                count += 1
            except:
                break
        return count

    def lessDel(self, i):
        temp = [int(x) for x in self.items]
        if(len(self.items) == 0):
            return -1
        ret = []
        while(len(temp) != 0):
            x = temp.pop(-1)
            if(x < i):
                self.items.remove(x)
                ret.append(x)
        return ret
        
    def moreDel(self, i):
        temp = [int(x) for x in self.items]
        if(len(self.items) == 0):
            return -1
        ret = []
        while(len(temp) != 0):
            x = temp.pop(-1)
            if(x > i):
                self.items.remove(x)
                ret.append(x)
        return ret
    
print("Enter Input : ",end='')
lst = [x.split() for x in input().split(',')]
stack = Stack()
for i in lst:
    if(i[0] == 'A'):
        stack.push(int(i[1]))
        print(f"Add = {i[1]}")
    elif(i[0] == 'P'):
        ret = stack.pop()
        if(ret == -1):
            print(-1)
        else: print(f'Pop = {ret}')
    elif(i[0] == 'D'):
        count = stack.delete(int(i[1]))
        if(count == -1):
            print('-1')
        else:
            for j in range(count):
                print(f'Delete = {i[1]}')
    elif(i[0] == "LD"):
        ret = stack.lessDel(int(i[1]))
        if(ret == -1):
            print('-1')
        else:
            for j in ret:
                print(f'Delete = {j} Because {j} is less than {i[1]}')
    elif(i[0] == "MD"):
        ret = stack.moreDel(int(i[1]))
        if(ret == -1):
            print("-1")
        else:
            for j in ret:
                print(f'Delete = {j} Because {j} is more than {i[1]}')

print(f'Value in Stack = {stack.items}')