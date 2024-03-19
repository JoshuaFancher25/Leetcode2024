# heap data structure is full binary tree represented in an array
# the child nodes of the ith parent node will be
# (2i + 1) and (2i + 2)
# arr = [1,2,3,4]
#       [0,1,2,3]

# a heap will either be a max heap or a min heap
# the default implementation in python is to have a min heap
# we need to import or libraries to use heaps in python

# the heap property is that every child node is >= to the parent in a min heap
# the minimum element is a the root
# the minimum value will always be the first element to be popped from the heap
# the time to create a min heap is O(n)
# the time remove and to add is O(logn) remove the element then maintain the heap property
# time to find the min element is O(1)

# heaps are great because we find the minimum or maximum element in O(1) time
# we can remove and add to the heap in O(logn) time - very very efficient
# We use heaps when we need more efficient code - avoids time limit exceeded - TLE

# to return the parent node or find the parent node is  (i-1)/2
from heapq import *

arr = [77, 44, 1, 7, 4, 15, 80, 20, 23,17,14 ]
print(1//2)
# in integer division the factional component is dropped
# we only care about the integer component of the division
print(arr)
heapify(arr)
print(arr)
heappop(arr)
print(arr)
heappop(arr)
print(arr)
heappush(arr, 1000)
print(arr)
heappush(arr, 5)
print(arr)
