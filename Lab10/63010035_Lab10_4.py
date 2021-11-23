class Data:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f"{self.key}"

class Hash:
    def __init__(self, size, maxCollision, threshold):
        self.size = size
        self.maxCollision = maxCollision
        self.threshold = threshold
        self.table = {}

    def insert(self, data):
        count = 1
        key = data.key % self.size

        while(True):
            #reach max collision
            if(count == self.maxCollision+1):
                print("****** Max collision - Rehash !!! ******")
                self.size = self.getNewSize()
                self.table = self.reHashing(data)
                self.printHashTable()
                return 0
            #no collision
            if(key not in self.table.keys()):
                #check if over threshold
                if(self.isOverThreshold()):
                    print("****** Data over threshold - Rehash !!! ******")
                    self.size = self.getNewSize()
                    self.table = self.reHashing(data)
                    self.printHashTable()
                else:
                    self.table.update({key: data})
                    self.printHashTable()
                return 0
            #collision occured
            else:
                print(f'collision number {count} at {key}')
                key = (data.key + (count*count)) % self.size
            count += 1

    def reHashing(self, newData):
        lst = [data for data in self.table.values()]
        lst.append(newData)
        dic = {}
        for data in lst:
            key = data.key % self.size
            count = 1
            while(True):
                if(key not in dic.keys()):
                    dic.update({key: data})
                    break
                else:
                    print(f'collision number {count} at {key}')
                    key = (data.key + (count*count)) % self.size
                count+=1
        return dic

    def getAscii(self, data):
        ret = 0
        for i in data.key:
            ret += ord(i)
        return ret

    def getNewSize(self):
        size = self.size * 2
        while(True):
            size+=1
            check = True
            for i in range(2, size):
                if(size % i == 0):
                    check = False
            if(check):
                return size

    def isFull(self):
        return len(self.table) == self.size

    def isOverThreshold(self):
        return len(self.table) >= int((self.threshold/100)*self.size)
    
    def printHashTable(self):
        for i in range(self.size):
            print(f'#{i+1}	',end='')
            if(i in self.table.keys()):
                print(f'{self.table[i]}')
            else:
                print("None")
        print("---------------------------")

print(" ***** Rehashing *****")
print("Enter Input : ",end='')
inp = [x for x in input().split('/')]
length, maxCollision, threshold = [int(x) for x in inp[0].split()]
data = [int(x) for x in inp[1].split()]
hashTable = Hash(length, maxCollision, threshold)
print("Initial Table : ")
hashTable.printHashTable()
for i in data:
    d = Data(i)
    print(f"Add : {d}")
    ret = hashTable.insert(d)