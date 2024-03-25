l = 0
r = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while l < len(arr):
    print(arr[l])
    while arr[l] != 3:
        print("testing our nested break", l)
        l += 1
        if l >= len(arr):  # Add a check to avoid index out of range
            break  # Break out of the inner loop if index exceeds length of arr
    else:
        l += 1
        break