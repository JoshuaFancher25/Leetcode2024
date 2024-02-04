# using the built-in sorting method in python
# sort makes changes to the underlying list
# must be careful if want to preserve structure of the underlying list

arr = [10,5,4,1,11,7,8,2]
print(arr)
arr.sort()
print(arr)
# the sort function changes the underlying structure of the list
# sort() method only works on list in python

# sorted() returns a sorted list but doesn't change the structure of the
# underlying list
# sorted to sort a set and dictionary for us
arr2 = [10,1,4,8,9,3,5,6]
print(arr2)
sorted(arr2)
print(arr2)

# method - says do something to this object
# function - does something - could be to an object - could be to integers
# class - blueprint for object creation 