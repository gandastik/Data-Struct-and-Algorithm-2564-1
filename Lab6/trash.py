def traversal(lst):
    if(len(lst) == 1):
        return lst[0]
    return traversal(lst[:-1])

def backtrack(k, start, nextStart, curr, arr, res, path):
    if(k == sum(path)):
        res.append([int(x) for x in path])
        return (start, curr, path)
    elif(sum(path) > k):
        return (start, curr, path)
    if(curr == len(arr)):
        return (start, curr, path)
    x = traversal(arr[curr:])
    path.append(x)
    return backtrack(k, start, nextStart, curr+1, arr, res, path)

def pantip(k, start, nextStart, curr, arr, res, path):
    if(start == len(arr)):
        return
    else:
        start, curr, path = backtrack(k, start, nextStart, curr, arr, res, path)
        if(curr == len(arr)):
            nextStart += 1
            curr = nextStart
            path = [path[0]]
        else: path.pop()
        if(path == []):
            start += 1
            nextStart = start+1
        if(nextStart >= len(arr) - 1):
            start += 1
            nextStart = start+1
            curr = start
            path = []
    pantip(k, start, nextStart, curr, arr, res, path)

            
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
res = []
pattern = pantip(int(inp[0]), 0, 0, 0, arr, res, [])
print(len(res))
print(res)
# print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], len(pattern)))