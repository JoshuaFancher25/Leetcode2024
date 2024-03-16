# we need to learn about heaps here

# a heaps is full binary tree that is represented in an array
# a heap must maintain the heap property where the parent is >= child - max heap
# heap can be created in O(n) time
# add O(logn)
# remove O(logn)
# find min/max O(1)

# from heapq import *
# we import all the methods/functions from heapq
# then we don't have to prefix each method with heapq we can just call the method
# heapify - O(n) time complexity
# heappush - O(logn) time complexity - add element to the heap
# heappop - O(logn) because we pop with is O(1) then we have to maintain the heap
#           - property which results in the O(logn) time complexity

from heapq import *

nums = [10,5,14,99,77,25,24]
print(nums)
heapify(nums)
print(nums)
heappush(nums, 33)
print(nums)
y = heappop(nums)
print(y)
print(nums)