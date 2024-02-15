# playing with sets

theSet = set()
print(type(theSet))
set2 = {1, 2,2, 3}
print(type(set2))

theSet.update([4,4,9,10])
print(theSet)

set1 = set()
set2 = set()

set1.update([1,2,3,4,5,1,1])
set2.update([4,5,6,7,8,9])
print(set1, set2)
print(set1 ^ set2) # symmetric difference
print(set1 - set2) # set difference
print(set1 | set2) # logical or
print(set1 & set2) # logical and