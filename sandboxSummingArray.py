# work with summing an array

arr = [1,2,3,4,5,6,7,8,9,10]
total = sum(arr)
print(total)
print(sum(arr))
print(sum(arr[1:2]))

# passed into the sum must be an iterable

# how to create a set
# create a set we can use the set() function
# -- using set function we would need to pass in an iterable
set2 = set(arr)
print(set2)
# or we can create using curly brackets theset = {}
theset = {1,2,3,4}
print(type(theset))
print(theset)
print(sum(theset))

# set symmetric difference ^
# set difference -
# set union |
# set intersction &
print(set2 & theset)