# making infinity in python

# I suppose i can see why it might be simpler to put a negative sign in front of the value
# just a little bit easier to use and understand


import math
print(math.inf)
print(-math.inf)
print(math.inf*-1)

arr = [12,11, 10, 9, 8, 5,11, 3]
arr2 = [i*-1 for i in arr]
print(arr2)
arr2.sort()

print(arr2)