from collections import deque

que = deque()

que.append(10)
que.append(100)
que.append(99)

print(que)
print(que.popleft())
print(que)