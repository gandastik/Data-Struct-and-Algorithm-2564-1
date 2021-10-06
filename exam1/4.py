def lstToStr(lst):
    s = ''
    for i in lst:
        s += i
    return s

print("*** String Rotation ***")
print("Enter 2 strings : ",end='')
firstString , secondString = [str(string) for string in input().split()]
firstLst = [x for x in firstString]
secondLst = [x for x in secondString]
strOutput1 = ""
strOutput2 = ""
count = 1
while(strOutput1 != firstString or strOutput2 != secondString):
    ret = firstLst.pop()
    firstLst.insert(0, ret)
    strOutput1 = lstToStr(firstLst)
    ret = secondLst.pop(0)
    secondLst.append(ret)
    strOutput2 = lstToStr(secondLst)
    if(count <= 5):
        print(f'{count} {strOutput1} {strOutput2}')
    count+=1
if(count > 7):
    print(" . . . . . ")
    print(f'{count-1} {strOutput1} {strOutput2}')
elif(count == 7):
    print(f'{count-1} {strOutput1} {strOutput2}')
if(len(firstString) != 0 and len(secondString) != 0):
    print(f"Total of  {count-1} rounds.")