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
            # self.inOrderRL(self.root, data)
            s = []
            curr = self.root
            while(True):
                if(curr is not None):
                    s.append(curr)
                    curr = curr.right
                    if(curr is None and s[-1].data in ['+', '-', '*', '/']):
                        s[-1].right = node
                        break
                    elif(curr is None and s[-1].data not in ['+', '-', '*', '/']):
                        pass
                elif(s):
                    curr = s.pop()
                    if(curr.data in ['+', '-', '*', '/'] and curr.left is None):
                        curr.left = node
                        break
                    curr = curr.left
                else:
                    break
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

    def inOrderRL(self, root, data):
        if(root is not None):
            self.inOrderRL(root.right, data)
            if(data in ['+', '-', '*', '/']):
                root.right = Node(data)
            self.inOrderRL(root.left, data)
            if(data not in ['+', '-', '*', '/']):
                root.left = Node(data)

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

def printLst(lst):
    s = ''
    for _ in lst:
        s += str(_)
    return s

def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

print("Enter Postfix : ",end='')
postfix = str(input())
stack = [str(x) for x in postfix]
# print(stack)
T = BST()
while(len(stack) != 0):
    ret = T.insert(stack.pop())
print("Tree : ")
T.printTree(ret)
preOrderLst = T.preOrder(ret, [])
# inOrderLst = T.inOrder(ret, [])
print('--------------------------------------------------')
print(f'Infix : {prefixToInfix(printLst(preOrderLst))}')
print(f'Prefix : {printLst(preOrderLst)}')