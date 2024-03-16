# we need to learn about heaps here

# a heaps is full binary tree that is represented in an array
# a heap must maintain the heap property where the parent is >= child - max heap
# heap can be created in O(n) time
# add O(logn)
# remove O(logn)
# find min/max O(1)

import heapq

nums = [10,5,14,99,77,25,24]
print(nums)
heapq.heapify(nums)
print(nums)
heapq.heappush(nums, 33)
print(nums)
y = heapq.heappop(nums)
print(y)
print(nums)