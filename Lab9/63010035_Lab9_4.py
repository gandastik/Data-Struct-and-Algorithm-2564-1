def quickSort(arr, left, right):
    if(left >= right):
        return
    pivot = arr[(left+right) // 2]
    index = partition(arr, left, right, pivot)
    quickSort(arr, left, index-1)
    quickSort(arr, index, right)

def partition(arr, left, right, pivot):
    while(left <= right):
        while(arr[left] < pivot):
            left+=1
        while(arr[right] > pivot):
            right-=1
        if(left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    return left
            

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    lst = []
    for i in range(0,len(l)):
        lst.append(l[i])
        quickSort(lst, 0, len(lst)-1)
        med = 0
        if(len(lst) % 2 == 0):
            left = int(len(lst) / 2) - 1
            right = int(len(lst) / 2)
            med = (lst[left] + lst[right]) / 2
        else:
            med = lst[(len(lst)//2)]
            # print(lst)
        print(f'list = {l[:i+1]} : median = {med:.1f}')