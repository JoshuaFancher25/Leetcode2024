# more practice with dictionaries

from collections import Counter

arr = [1,1,1,3,3,3,5,5,5,5,8,8]
# how to sort by both frequency and integer value in python
dic = Counter(arr)
print(dic)
print(dic.keys())
print(dic.values())
