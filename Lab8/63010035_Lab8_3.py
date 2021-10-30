class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
class Tree:
    def __init__(self, root=None, n=0):
        self.root = root
        self.n = n

        #initiate the Tree from N
        for i in range(n//2):
            self.insert(0)
    
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

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def postOrder(self, root):
        if(root is not None):
            self.postOrder(root.left)
            self.postOrder(root.right)
            minValue = 0
            if(root.left and root.right):
                minValue = min(root.left.val, root.right.val)
                root.left.val -= minValue
                root.right.val -= minValue
                root.val = minValue
            elif(root.left and not root.right):
                minValue = root.left.val
                root.left.val -= minValue
                root.val = minValue
            elif(root.right and not root.left):
                minValue = root.right.val
                root.right.val -= minValue
                root.val = minValue

    def preOrder(self, root, lst):
        if(root is not None):
            lst.append(root.val)
            self.preOrder(root.left, lst)
            self.preOrder(root.right, lst)
        return lst
    
    def getRoot(self):
        return self.root

print("Enter Input : ",end='')
inp = [x.split() for x in input().split('/')]
n = int(inp[0][0])
nodes = [int(x) for x in inp[1]]
if(len(nodes) != (n//2)+1):
    print("Incorrect Input")
# print(n)
# print(nodes)
# print(inp)
else:
    T = Tree(n=n)
    for i in nodes:
        T.insert(i)
    T.postOrder(T.getRoot())
    lst = T.preOrder(T.getRoot(), [])
    print(sum(lst))