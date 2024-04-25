#testing range printing
k = 2
for i in range(k):
    print(i)

nums = [10,11, 100, 5, 9, 15, 16, 20, 21, 22, 55, 77, 88]
from heapq import *
heapify(nums)
print(nums)
print(heappop(nums))
heappush(nums, 2)
print(nums)