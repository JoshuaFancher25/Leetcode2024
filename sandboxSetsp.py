# learning about sets

x = {1,2,3,4,5,6,7}
y = {3,4,5,6,7,8,9}

print(x | y) # set union

print(x & y) # set intersection

print(x - y) # set difference
print(y - x) # set difference

print(x ^ y) # symmetric difference - elements that are not in both
print(x.symmetric_difference(y)) # elements that are not in both sets


print(x.isdisjoint(x))  # only if both sets don't have elements in common