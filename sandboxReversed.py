# learning how the reversed function works

arr = [1,2,3,4,5,6,7,8,9]
# this returns an iterator it doesn't reverse the list in place
# we must do list slicing to reverse in place
reversed(arr)

print(arr[::-1])
arr = arr[::-1]
print(arr)
# slice notation [start:stop(not inclusive): step]
# when we have a negative step value then we are going in reverse
arr2 = [1,2,3,4,5]
print(arr2[2::-1])
# negative step value means we go in reverse
#### NEGATIVE STEP MEANS SLICING IS IN REVERSE ORDER ####
