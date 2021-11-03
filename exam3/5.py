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

    def preOrder(self, root, ret):
        if(root is not None):
            ret.append(root.data)
            self.preOrder(root.left, ret)
            self.preOrder(root.right, ret)
        return ret

    def inOrder(self, root, ret):
        if(root is not None):
            self.inOrder(root.left, ret)
            ret.append(root.data)
            self.inOrder(root.right, ret)
        return ret

    def postOrder(self, root, ret):
        if(root is not None):
            self.postOrder(root.left, ret)
            self.postOrder(root.right, ret)
            ret.append(root.data)
        return ret

    def BFS(self, root):
        q = [root]
        ret = []
        while(len(q) != 0):
            curr = q.pop(0)
            ret.append(curr.data)
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
        return ret

print(" *** Binary Search Tree ***")
print("Enter Input : ", end='')
inp = [int(x) for x in input().split()]
root = None
Tree = BST()
for i in inp:
    root = Tree.insert(i)
print("")
print(" --- Tree traversal ---")
print('Level order :', *Tree.BFS(root))
print("Preorder :", *Tree.preOrder(root, []))
print("Inorder :", *Tree.inOrder(root, []))
print("Postorder :", *Tree.postOrder(root, []))