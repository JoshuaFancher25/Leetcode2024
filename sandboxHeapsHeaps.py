# memorizing how to use heaps
# heap creation is O(n) time
# find min/max O(1)
# add O(logn)
# delete O(logn)
# by default in python a heap is structured as an array
# but is in binary tree for mat.
# the ith nodes children can be found at
# - (2i + 1)  and at (2i + 2)
# i = 0 -- means children node at 1 and 2
# i = 1 == meands children at 3 and 4
# i = 2 -- means children at 5 and 6

from heapq import *
nums = [12,1,4,99,44, 43, 55, 67, 31, 24, 25]
print(nums)
heapify(nums)
print(nums)
# to create a max heap we need to multiply all values by -1
for i in range(len(nums)):
    nums[i] *= -1
print(nums)
heapify(nums)
print(nums)
print(heappop(nums))
print(nums)
heappush(nums, 1000)
print(nums)
heappush(nums, -5000)
print(nums)