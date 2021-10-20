class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = ''
        p = self.head
        while p.next != None :
            s += str(p.data)+ ' <- '
            p = p.next
        s += str(p.data)
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def reOrder(self):
        temp = self.head
        node = None
        count = 0
        while(temp):
            if(temp.data == 0):
                node = temp
                break
            temp = temp.next
            count += 1
        temp = self.head
        if(count == 0):
            return
        for i in range(count-1):
            temp = temp.next
        temp.next = None
        ll = LinkedList(node)
        temp = self.head
        while(temp):
            ll.append(temp.data)
            temp = temp.next
        self.head = ll.head

print(" *** Re order ***")
print("Enter Input : ", end="")
lst = [int(x) for x in input().split()]
ll = LinkedList()
for i in lst:
    ll.append(i)
print(f"Before : {ll} ")
ll.reOrder()
print(f'After : {ll}')