class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Tree Structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Tree Traversal Techniques
'''
# DFS
    1.pre-order(root left right)
    2.in-order(left root right)
    3.post-order(left right root)

# BFS(level order)
'''


def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')


print("PreOrder: ", end="")
preOrder(root)
print()

print("InOrder: ", end="")
inOrder(root)
print()

print("PostOrder: ", end="")
postOrder(root)
print()
