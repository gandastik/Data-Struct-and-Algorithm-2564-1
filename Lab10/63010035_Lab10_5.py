def minimum_weight(items,box):
    if box == 1:
        return sum(items)
    min_weight = 99999999999999
    for index in range(len(items)):
        if len(items[index:]) < box -1:
            break
        this_box = sum(items[:index])
        other_box = minimum_weight(items[index:],box -1)
        min_weight = min(max(this_box,other_box), min_weight)

    return min_weight

print("Enter Input : ",end='')
inp = [x for x in input().split('/')]
stuff = [int(item) for item in inp[0].split()]
boxes = int(inp[1])
print(f'Minimum weigth for {boxes} box(es) = {minimum_weight(stuff, boxes)}')
