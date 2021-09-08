class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        s = ''
        temp = self.head
        if(self.isEmpty()):
            return ''
        else:
            while(temp.next):
                s += str(temp.val) + '->'
                temp = temp.next
            s+= str(temp.val)
        return s

    def str_reverse(self):
        s = ''
        temp = self.head
        if(self.isEmpty()):
            return ''
        while(temp.next):
            temp = temp.next
        while(temp.prev):
            s += str(temp.val) + '->'
            temp = temp.prev
        s += str(temp.val)
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
            node.prev= temp
            temp.next = node
            self.size += 1
        
    def insert(self, index, val):
        temp = self.head
        count = 0
        if(index < 0 or index > self.size):
            return -1
        if(index == 0):
            if(self.isEmpty()):
                node = Node(val)
                self.head = node
                self.size += 1
            else:
                node = Node(val)
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.size += 1
        while(temp):
            if(count == index - 1):
                if(count == self.size - 1):
                    node = Node(val)
                    node.prev = temp
                    node.next = temp.next
                    temp.next = node
                    self.size += 1
                else:
                    node = Node(val)
                    node.prev = temp
                    node.next = temp.next
                    temp.next.prev = node
                    temp.next = node
                    self.size += 1
            count += 1
            temp = temp.next

    def remove(self, val):
        if(self.isEmpty()):
            return -1 
        else: 
            index = 0
            if(self.head.val == val):
                if(self.size == 1):
                    nextNode = self.head.next
                    self.head = nextNode
                    self.size -=1
                    return 0
                else:
                    nextNode = self.head.next
                    self.head = nextNode
                    nextNode.prev = None
                    self.size -= 1
                    return 0
            temp = self.head
            while(temp):
                if(temp.val == val):
                    prevNode = temp.prev
                    temp.next.prev = prevNode
                    prevNode.next = temp.next
                    self.size -= 1
                    return index
                temp = temp.next
                index += 1
        return -1

print("Enter Input : ", end='')
lst = [x.split() for x in input().split(',')]
llist = DoublyLinkedList()

valToInsert = []
idxToInsert = []

for i in lst:
    if(i[0] == "I"):
        for j in range(len(i[1])):
            if(i[1][j] == ':'):
                idxToInsert.append(int(i[1][:j]))
                valToInsert.append(int(i[1][j+1:]))

count = 0
for item in lst:
    if(item[0] == 'A'):
        llist.append(int(item[1]))
        print(f'linked list : {llist}')
        print(f'reverse : {llist.str_reverse()}')
    elif(item[0] == "Ab"):
        llist.insert(0, int(item[1]))
        print(f'linked list : {llist}')
        print(f'reverse : {llist.str_reverse()}')
    elif(item[0] == 'I'):
        ret = llist.insert(idxToInsert[count], valToInsert[count])
        if(ret == -1):
            print("Data cannot be added")
            print(f'linked list : {llist}')
            print(f'reverse : {llist.str_reverse()}')
        else:
            print(f'index = {idxToInsert[count]} and data = {valToInsert[count]}')
            print(f'linked list : {llist}')
            print(f'reverse : {llist.str_reverse()}')
        count+=1
    elif(item[0] == 'R'):
        ret = llist.remove(int(item[1]))
        if(ret == -1):
            print("Not Found!")
            print(f'linked list : {llist}')
            print(f'reverse : {llist.str_reverse()}')
        else:
            print(f'removed : {item[1]} from index : {ret}')
            print(f'linked list : {llist}')
            print(f'reverse : {llist.str_reverse()}')