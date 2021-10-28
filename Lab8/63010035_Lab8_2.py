class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if(self.root is None):
            self.root = node
        else:
            stack = [self.root]
            #DFS search to find the proper left node for a target node and insert a node as a left node
            while(len(stack) != 0):
                top = stack.pop()
                #if the input data is less than the current node data
                if(node.data < top.data):
                    #check if there's left node
                    if(top.left):
                        stack.append(top.left)
                    #if there's no left node anymore (we're at the external node)
                    else:
                        #add the left node
                        top.left = node
                #if the input data more than or equal to the current node data
                elif(node.data >= top.data):
                    #check if there's right node
                    if(top.right):
                        stack.append(top.right)
                    #if there's not right node anymore (we're at the external node)
                    else:
                        #add the left node
                        top.right = node
        return self.root

    def search(self, root, data):
        s = [root]
        while(len(s) != 0):
            curr = s.pop()
            if(data < curr.data):
                s.append(curr.left)
                if(curr.left is None):
                    return curr.data
            elif(data > curr.data):
                s.append(curr.right)
                if(curr.right is None):
                    return curr.data
            else:
                return curr.data

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def inorder(root, lst):
    if(root):
        inorder(root.left, lst)
        lst.append(root.data)
        inorder(root.right, lst)
    return lst

print("Enter Input : ",end='')
inp = [x.split() for x in input().split('/')]
nums = [int(x) for x in inp[0]]
find = int(inp[1][0])
tree = BST()
root = Node()
for i in nums:
    root = tree.insert(i)
    tree.printTree(root)
    print("--------------------------------------------------")
found = -2000000000000000000
for i in inorder(root, []):
    if(i >= find):
        found = i
        break
found2 = tree.search(root, find)
if(found >= found2):
    print(f'Closest value of {find} : {found}')
else:
    print(f'Closest value of {find} : {found2}')