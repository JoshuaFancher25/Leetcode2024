class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

a = Node(10)
print(a.val)
b = Node(15)
a.left= b
print(a.left.val)