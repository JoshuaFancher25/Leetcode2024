# internalizing the length function
arr = [12,13,14,15,16,17,18,19,20,21]
print(len(arr))
# remember we are dealing with 0 indexes
# 0 is a symbol in the decimal system of counting
# the length will return the number of elements in the array
# but the array itself has a 0th element
print(arr[8])
for i in range(len(arr)):
    print("this is position: ",i,"with value:", arr[i])
