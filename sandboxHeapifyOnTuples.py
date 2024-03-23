# using heapify on a list of tuples
arr = [1,2,3,4,5,6,7,8,9]
arr2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
out = []
for i in range(len(arr)):
    out.append((arr[i], arr2[i]))
print(out)
out2 = out[::-1]
print(out2)
from heapq import *
heapify(out2)
print(out2)

# the elements in an array should be comparable to use the heapify method
# we can tuples and heaps to work with our greedy algorithms
# are we talking a data structure or our algorithm
# we can use data structures in our algorithm to solve our coding problems.