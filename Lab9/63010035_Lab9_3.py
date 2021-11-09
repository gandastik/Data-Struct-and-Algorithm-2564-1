def sortA(nums):
    for i in range(len(nums)):
        minIndex = i
        for j in range(i+1, len(nums)):
            if(nums[minIndex] > nums[j]):
                minIndex = j
        nums[minIndex], nums[i] = nums[i], nums[minIndex]
    
def sortD(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] < nums[j]):
                nums[i], nums[j] = nums[j], nums[i]

def hasDup(nums):
    return len(nums) != len(set(nums))

print("Enter Input : ",end='')
inp = [int(x) for x in str(input())]
str_input = ''.join(str(x) for x in inp)
sortA(inp)
strAscending = ''.join(str(x) for x in inp)
sortD(inp)
strDecending = ''.join(str(x) for x in inp)
if(str_input == strAscending and str_input == strDecending):
    print("Repdrome")
elif(str_input == strAscending and hasDup(inp) == False):
    print("Metadrome")
elif(str_input == strAscending and hasDup(inp)):
    print("Plaindrome")
elif(str_input == strDecending and hasDup(inp) == False):
    print("Katadrome")
elif(str_input == strDecending and hasDup(inp)):
    print("Nialpdrome")
else:
    print("Nondrome")