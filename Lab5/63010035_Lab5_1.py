class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        s = ''
        temp = self.head
        if(self.isEmpty()):
            return 'List is empty'
        else:
            while(temp.next):
                s += str(temp.val) + '->'
                temp = temp.next
            s+= str(temp.val)
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, val):
        node = Node(val)
        if(self.head == None):
            self.head = node
            self.size += 1
        else :
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node
            self.size += 1

    def insert(self, index, val):
        temp = self.head
        count = 0
        if(index < 0 or index > self.size):
            return -1
        if(index == 0):
            node = Node(val)
            node.next = self.head
            self.head = node
            self.size += 1
        while(temp):
            if(count == index - 1):
                node = Node(val)
                node.next = temp.next
                temp.next = node
                self.size += 1
            count += 1
            temp = temp.next

print("Enter Input : ", end='')
input_lst = [x.split() for x in input().split(',')]
llist = LinkedList()
# print(input_lst)
#iterate through initial command
for i in input_lst[0]:
    llist.append(int(i))

valToAdd = []
idxToAdd = []

for i in range(1, len(input_lst)):
    for j in range(len(input_lst[i][0])):
        if(input_lst[i][0][j] == ':'):
            idxToAdd.append(int(input_lst[i][0][:j]))
            valToAdd.append(int(input_lst[i][0][j+1:]))

if(llist.isEmpty()):
    print(llist)
else: 
    print(f'link list : {llist}')
for i in range(len(valToAdd)):
    ret = llist.insert(idxToAdd[i], valToAdd[i])
    if(ret == -1):
        print('Data cannot be added')
        if(llist.isEmpty()):
            print(llist)
        else: 
            print(f'link list : {llist}')
    else:
        print(f'index = {idxToAdd[i]} and data = {valToAdd[i]}')
        if(llist.isEmpty()):
            print(llist)
        else: 
            print(f'link list : {llist}')