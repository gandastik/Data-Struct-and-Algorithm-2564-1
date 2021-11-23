def printHashTable(length, dic):
    for i in range(length):
        print(f"#{i+1}	",end='')
        if(i in dic.keys()):
            print(f'{dic[i]}')
        else:
            print("None")
    print("----------------------------------------")

def findNextPrime(length):
    length *= 2
    while(True):
        length+=1
        check = True
        for i in range(2,length):
            if(length % i == 0):
                check = False
        if(check):
            return length
        
def hashing(length, dic, data):
    for i in data:
        key = i % length
        count = 1
        while(True):
            if(key not in dic.keys()):
                dic.update({key: i})
                break
            else:
                print(f'collision number {count} at {key}')
                key = (i + (count*count)) % length
            count+=1
    return dic

print(" ***** Rehashing *****")
print("Enter Input : ",end='')
inp = [x for x in input().split('/')]
length, maxCollision, threshold = [int(x) for x in inp[0].split()]
data = [int(data) for data in inp[1].split()]
dic = {}
# print(length, maxCollision, threshold)
# print(data)
print("Initial Table :")
printHashTable(length, dic)
lst = []
for i in data:
    print(f"Add : {i}")
    key = i % length
    count = 1
    lst.append(i)
    while(True):
        if(count == maxCollision+1):
            print("****** Max collision - Rehash !!! ******")
            length = findNextPrime(length)
            # key = i % length
            # dic.update({key: i})
            dic.clear()
            dic = hashing(length, dic, lst)
            printHashTable(length, dic)
            break
        if(key not in dic.keys()):
            if(len(dic) >= int((threshold/100)*length)):
                print("****** Data over threshold - Rehash !!! ******")
                length = findNextPrime(length)
                # key = i % length
                # dic.update({key: i})
                dic.clear()
                dic = hashing(length, dic, lst)
                printHashTable(length, dic)
            else:
                dic.update({key: i})
                printHashTable(length, dic)
            break
        else:
            print(f'collision number {count} at {key}')
            key = (i + (count*count)) % length
        count+=1
