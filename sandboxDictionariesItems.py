# playing with dictionaries and using the items

# can import the counter in python to get super fast way to create a count dictinary
from collections import Counter

arr = [1,1,1,2,2,3,4,5,5,5,5,5]
dic = Counter(arr)
print(dic)

# can do it the old fashioned way and iterate through the dictionary
dic2 = {}
arr2 = [10,10,10,11,11,15,15,15,15,15]
for num in arr2:
    dic2[num] = dic2.get(num, 0) + 1
print(dic2)

# to iterate over the key and value in the dictionary use dic.items
for key, value in dic2.items():
    print(key, ":", value)