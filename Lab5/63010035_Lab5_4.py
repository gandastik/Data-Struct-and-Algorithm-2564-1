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
        
    def lookBack(self):
        if(self.isEmpty()):
            return 0
        temp = self.head
        while(temp.next):
            temp = temp.next
        _max = temp.val
        count = 1
        while(temp):
            if(temp.val > _max):
                _max = temp.val
                count += 1
            temp = temp.prev
        return count

print("Enter Input : ", end='')
lst = [x.split() for x in input().split(',')]
llist = DoublyLinkedList()
for item in lst:
    if(item[0] == 'A'):
        llist.append(int(item[1]))
    elif(item[0] == 'B'):
        print(llist.lookBack())