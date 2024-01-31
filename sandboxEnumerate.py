# learning enumerate

# Enumerate gives us the index and the value
# very helpful operation


arr = [10,20,30,40,50,60,70,80,90]
for i, j in enumerate(arr):
    print(i, " : ", j)

# we can enumerate a dictionary
from collections import Counter
dic = Counter(arr)
print(dic)
for i, j in enumerate(dic):
    print(i, " : ", j)