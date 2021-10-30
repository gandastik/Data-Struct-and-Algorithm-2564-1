class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.total = val
    
    def __str__(self):
        return str(self.val)

class LevelOrderTree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, val):
        newNode = Node(val)
        if(self.root is None):
            self.root = newNode
        else:
            q = [ self.root ]
            while(len(q) != 0):
                curr = q.pop(0)
                if(curr.left):
                    q.append(curr.left)
                else:
                    curr.left = newNode
                    break
                if(curr.right):
                    q.append(curr.right)
                else:
                    curr.right = newNode
                    break
        return self.root

    def BFS(self, lst):
        q = [self.root]
        while(len(q) != 0):
            curr = q.pop(0)
            lst.append(curr.total)
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
        return lst 
    
    def postOrder(self, root):
        if(root is not None):
            self.postOrder(root.left)
            self.postOrder(root.right)
            if(root.left):
                root.total += root.left.total
            if(root.right):
                root.total += root.right.total

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
print("Enter Input : ",end='')
inp = [x for x in input().split('/')]
nodes = [int(x) for x in inp[0].split()]
commands = [x.split() for x in inp[1].split(',')]
T = LevelOrderTree()
root = None
for i in nodes:
    root = T.insert(i)
T.postOrder(root)
T.printTree(root)
BFSLst = T.BFS([])
print(BFSLst)
print(BFSLst[0])
for command in commands:
    if(BFSLst[int(command[0])] > BFSLst[int(command[1])]):
        print(f'{command[0]}>{command[1]}')
    elif(BFSLst[int(command[0])] < BFSLst[int(command[1])]):
        print(f'{command[0]}<{command[1]}')
    else:
        print(f'{command[0]}={command[1]}')