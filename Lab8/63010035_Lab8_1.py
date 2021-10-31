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

    def inOrder(self, root, dic, encoded):
        if(root.left is None and root.right is None):
            dic.update({root.symbol : encoded})
        else:
            if(root.right is not None):
                encoded += '1'
                self.inOrder(root.right, dic, encoded)
            encoded = encoded[:-1]
            if(root.left is not None):
                encoded += '0'
                self.inOrder(root.left, dic, encoded)
        return dic

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
# print(dic)
nodes = [Node(dic[x], x) for x in dic.keys()]
while(len(nodes) > 1):
    check = False
    #sort the nodes based on their frequency and symbol
    nodes = sorted(nodes, key=lambda x: (x.freq, x.symbol))
    left = nodes[0]
    right = nodes[1]
    if(left.symbol == ' ' and right.symbol == '*'):
        left = nodes.pop(0)
        nodes.append(left)
        left = nodes[0]
        right = nodes[1]
    newNode = Node(freq=left.freq+right.freq, left=left, right=right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)


root = Tree(nodes[0])
encodedTable = root.inOrder(nodes[0], {}, '')
print(encodedTable)
root.printTree(nodes[0])
encodedWord = ''
for i in word:
    encodedWord += encodedTable[i]
print(f"Encoded! : {encodedWord}")