class Node:
    def __init__(self, data):
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

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)