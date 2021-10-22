class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r,data):
    s = [r]
    if(r.data == data):
        return -1
    while(len(s) != 0):
        top = s.pop()
        if(top.left):
            s.append(top.left)
            if(top.left.data == data):
                return top.data
        if(top.right):
            s.append(top.right)
            if(top.right.data == data):
                return top.data




tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
ret = father(tree.root,data[1])
if(ret == -1):
    print(f'None Because {data[1]} is Root')
elif(ret is None):
    print('Not Found Data')
else:
    print(ret)