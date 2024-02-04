# nested for loop
arr = [2,3,4,5,6]
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        print("Outer loop - ", i, " : ", "Inner Loop - ", j )
for idx, val in enumerate(arr):
    print("Index value : ", idx, " -- Value : ", val)
