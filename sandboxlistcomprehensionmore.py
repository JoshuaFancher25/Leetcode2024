# Learning more list comprehension
# a handy feature for generating elements in a a python list

out = [i for i in range(10)]
print(out)
out2 = [-i*2 for i in out]
print(out2)
out3 = [i if i%2 == 0 else "not divisible" for i in out]
print(out3)
from heapq import *
from heapq import *
heapify(out2)
print(out2)
heappop(out2)
print(out2)
# must maintain the heap property - every child node is greater than or equal to the parent node
