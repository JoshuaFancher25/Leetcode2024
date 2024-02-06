
import math
def pickGifts(gifts, k) -> int:
    # this is going to take a for loop with k iterations
    # we will replace the highest value in the array
    # i think we can do it as a single pass... no because if k is longer than the array
    # a single pass won't work
    # at the end we just need a sum of the entire array
    iteration = 0
    while iteration < k:
        maxindex = 0
        for i in range(len(gifts)):
            if gifts[maxindex] < gifts[i]:
                maxindex = i
                print(maxindex)

        gifts[maxindex] = math.floor(gifts[maxindex] ** 0.5)
        print(gifts)

        iteration += 1
        print("iteration : ", iteration)
    return sum(gifts)

gifts = [25,64,9,4,100]
k = 4

print(pickGifts(gifts, k))