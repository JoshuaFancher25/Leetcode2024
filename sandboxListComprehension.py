# playing around with list comprehension

arr = [0,1,1,3,0,5]
newarr = [i for i in arr if i > 0]
print(arr)
print(newarr)

def removezero(arr):
    out = []
    for i in arr:
        if i > 0:
            out.append(i)
    return out
print(removezero(arr))

import math
print(type(math.inf))
print(math.inf)