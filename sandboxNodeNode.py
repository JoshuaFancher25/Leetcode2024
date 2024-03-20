# creating a node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = Node(10)
root.right = Node(15)
root.left = Node(20)

print(root.right.val)