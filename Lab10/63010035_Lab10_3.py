def printHashTable(length, dic):
    for i in range(length):
        print(f"#{i+1}	",end='')
        if(i in dic.keys()):
            print(f'({dic[i][0]}, {dic[i][1]})')
        else:
            print("None")
    print("---------------------------")

print(" ***** Fun with hashing *****")
print("Enter Input : ",end='')
inp = [x for x in input().split('/')]
length, maxCollision = [int(x) for x in inp[0].split()]
data = [data.split() for data in inp[1].split(',')]
dic = {}
for i in data:
    _sum = 0
    count = 1
    for j in i[0]:
        _sum += ord(j)
    key = _sum%length
    if(len(dic) >= length):
        print("This table is full !!!!!!")
        break
    while(True):
        if(count == maxCollision+1):
            print("Max of collisionChain")
            printHashTable(length, dic)
            break
        if(key not in dic.keys()):
            dic.update({key: i})
            # print(dic)
            printHashTable(length, dic)
            break
        else:
            print(f"collision number {count} at {key}")
            key = (_sum + (count*count)) % length
        count += 1