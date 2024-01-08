alist = []
print(not alist)
alist.append(10)
print(not alist)

from collections import deque
stack = deque()
print(type(stack))
stack.append(100)
print(not stack)
print(stack)