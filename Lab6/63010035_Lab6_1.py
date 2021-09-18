def findMax(nums, n):
    if(n == 1):
        return nums[0]
    else:
        return max(nums[n-1], findMax(nums, n-1))

print("Enter Input : ",end = '')
nums = [int(x) for x in input().split()]
print(f'Max : {findMax(nums, len(nums))}')