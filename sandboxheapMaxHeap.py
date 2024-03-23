# creating a max heap in python
# the default behavior in python is a min_heap therfore,
# to create a max_head you have to multiply each value being inserted by a negative value
arr = [10,1,2,3,4,5,100,500,250,123]

# this is a list comprehension - enable us to create a new list in one line of code
# very convenient very fast way of doing our code that doesn't require and explict for loop
arr2 = [i*-1 for i in arr]
print(arr2)
from heapq import *
heapify(arr2)
print(arr2)
heappop(arr2)
print(arr2)
heappop(arr2)
print(arr2)
heappush(arr2, -1000)
print(arr2)
# must remember our heap is a max heap therfore, the value needs to be negative
heappush(arr2, -300)
print(arr2)

arr3 = [i*-1 for i in arr2]
print(arr3)
heapify(arr3)
# super important here.... this is a shallow copy...
# too get a full copy we need to call the deepcopy method

from copy import deepcopy

# we can really see the difference in importing the deepcopy here in this code.
# if we don't us the deepcopy the modification we make are having a effect on all
# the arrays that were copied later on in the code.
min_heap = arr3
print(min_heap)
arr3[0] = 5000
print(arr3)
print(min_heap)
min_heap2 = deepcopy(arr3)
print(min_heap2)
arr3[-1] = 555
print(arr3)
print(min_heap)
print(min_heap2)

min_heap[0] = 1999

print(arr3)
print(min_heap)

# shallowcopy - copies references to objects - it doesn't actually copy the object
#               - thus if changes are made to the original object then the values
#               - of all subsequent objects will be changed as well all objects that
#               - reference that copy will be changed - unexpected changes occur in
#               - copies of the object

# a = b - simply creates a new reference to the same object.

# heapfiy - mutates the original array and arranges the elements to satify the heap propterty
# heapy property - min_heap all elements in the left and right subtrees are <= to the parent
# heap is created in O(n) time -
# max/min element is retrieved in O(1) time
# add / delete is O(logn) -
# heap property for a binary heap - the min element is at the root
# heap property ensure that the root node contains the minimum element
# giving efficient access to the minium element
# heap is a complete binary tree that maintains the heap property