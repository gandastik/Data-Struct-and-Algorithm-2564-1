print(" *** String count ***")
string = str(input("Enter message : "))
upperCount = 0
uppers = []
lowerCount = 0
lowers = []
for i in string:
    if(i.isupper()):
        upperCount+=1
        if(i not in uppers):
            uppers.append(i)
    elif(i.islower()):
        lowerCount+=1
        if(i not in lowers):
            lowers.append(i)

uppers.sort()
lowers.sort()
print(f"No. of Upper case characters : {upperCount}")
print(f"Unique Upper case characters : ",end='')
for i in uppers:
    print(i, end='  ')
print(f"\nNo. of Lower case Characters : {lowerCount}")
print(f"Unique Lower case characters : ", end='')
for i in lowers:
    print(i, end='  ')