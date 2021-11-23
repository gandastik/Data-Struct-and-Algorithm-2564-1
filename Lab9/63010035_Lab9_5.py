def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def combination(arr):
    def findSum(arr, n):
        if n == 0:
            return [[]]
        lst = list()
        for i in range(len(arr)):
            strt = arr[i]
            rem = arr[i + 1 :]
            for j in findSum(rem, n - 1):
                lst.append(sort([strt] + j))
        return sort(lst)

    res = list()
    for i in range(1, len(arr) + 1):
        res.extend(findSum(arr, i))
    return res


inp = input("Enter Input : ").split("/")
num = int(inp[0])
lst = [int(x) for x in inp[1].split()]
sublst = combination(lst)
res = []
for i in sublst:
    if sum(i) == num:
        res.append(i)
if res:
    for i in res:
        print(i)
else:
    print("No Subset")