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
            return 'Empty'
        else:
            while(temp):
                s += str(temp.val)
                temp = temp.next
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

def checkCrush(llist):
    temp = llist.head
    curr = None
    count = 0
    idx = 0
    combo = 0
    crush = False
    while(temp):
        if(curr == temp.val):
            count += 1
        else:
            curr = temp.val
            count = 1
        if(count == 3):
            t = llist.head
            for i in range(idx-3):
                t = t.next
            try:
                t.next = t.next.next.next.next
            except:
                llist.head = None
                llist.size -= 3
                combo += 1
                return combo
            llist.size -= 3
            idx = 0
            temp = llist.head
            curr = temp.val
            count = 1
            combo += 1
        idx += 1
        temp = temp.next
    return combo

print("Enter Input : ", end='')
lst = [x for x in input().split()]
llist = LinkedList()
for i in range(len(lst) - 1, -1, -1):
    llist.append(lst[i])

combo = checkCrush(llist)
print(f'{llist.size}')
print(llist)
if(combo > 1):
    print(f'Combo : {combo} ! ! !')