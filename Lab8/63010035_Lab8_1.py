class Node:
    def __init__(self, freq=0,symbol='*', left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.symbol)

class Tree:
    def __init__(self, root=None):
        self.root = root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

print("Enter Input : ",end='')
word = str(input(""))
dic = {}
for i in word:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
items = sorted(dic.items())
dic = dict(items)
dic = dict(sorted(dic.items(), key=lambda item: item[1]))
print(dic)
nodes = [Node(dic[x], x) for x in dic.keys()]
while(len(nodes) > 1):
    #sort the nodes based on their frequency
    check = False
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    newNode = Node(freq=left.freq+right.freq, left=left, right=right)
    nodes.remove(left)
    nodes.remove(right)
    if(nodes[-1].freq == newNode.freq):
        nodes.append(newNode)
    else:
        nodes.insert(1, newNode)


root = Tree(nodes[0])
root.printTree(nodes[0])