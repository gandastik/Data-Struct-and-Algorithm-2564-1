class Node:
    def __init__(self, val=0, id=0):
        self.val = val
        self.id = id

print("Enter Input : ",end='')
inp = [x.split() for x in input().split('/')]
n = int(inp[0][0])
q = [int(x) for x in inp[1]]
lst = []
for i in range(n):
    lst.append(Node(id=i+1))

for i in range(len(q)):
    print(f'Customer {i+1} Booking Van {lst[0].id} | {q[i]} day(s)')
    lst[0].val += q[i]
    lst = sorted(lst, key=lambda x: (x.val, x.id))