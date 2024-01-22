# we are incrementing an array
arr = [1,2,3]
for i in range(len(arr)-1, -1, -1):
    arr[i] += 1
print(arr)

for i in range(2, -1):
    print(i)