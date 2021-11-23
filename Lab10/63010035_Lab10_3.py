class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size, maxCollision):
        self.size = size
        self.maxCollision = maxCollision
        self.table = {}

    def insert(self, data):
        count = 1
        key = self.getAscii(data) % self.size
        #check if talbe full
        if(self.isFull()):
            print("This table is full !!!!!!")
            return -1

        #check collision
        while(True):
            if(count == self.maxCollision+1):
                print("Max of collisionChain")
                self.printHashTable()
                return 0
            if(key not in self.table.keys()):
                self.table.update({key: data})
                self.printHashTable()
                return 0
            else:
                print(f'collision number {count} at {key}')
                key = (self.getAscii(data) + (count*count)) % self.size
            count += 1
        #insert data

    def getAscii(self, data):
        ret = 0
        for i in data.key:
            ret += ord(i)
        return ret

    def isFull(self):
        return len(self.table) == self.size
    
    def printHashTable(self):
        for i in range(self.size):
            print(f'#{i+1}	',end='')
            if(i in self.table.keys()):
                print(f'{self.table[i]}')
            else:
                print("None")
        print("---------------------------")


print(" ***** Fun with hashing *****")
print("Enter Input : ",end='')
inp = [x for x in input().split('/')]
size, maxCollision = [int(x) for x in inp[0].split()]
data = [x.split() for x in inp[1].split(',')]
hashTable = Hash(size, maxCollision)
for item in data:
    d = Data(item[0], item[1])
    ret = hashTable.insert(d)
    if(ret == -1):
        break
    
# hashTable.printHashTable()