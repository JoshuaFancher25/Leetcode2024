# using deque
# technically pronounced as "deck"
# but I like deque
from collections import deque
stack = deque()
print(type(stack))

stack.append(100)
stack.append(1000)
stack.append("A")

print(stack)
print(stack[-1])
stack.pop()
for element in stack:
    print(element)
print()
def something( x) -> bool:
    print(x + 10)

something(10)