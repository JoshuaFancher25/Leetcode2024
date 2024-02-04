

# sort by value and frequency
arr = [3,3,3,1,5,5,2,0, 0 , 0 , 0]
from collections import Counter
dic = Counter(arr)
print(dic)
# can't use this because sort only works on lists?
# sort is a method of the list class and can only be used on lists
# we would have to change the dictionary to a list. then use the key
# dic.sort(key = lambda x: (x[1], x[0]))

arr2 = ["a", "a", "a", "c", "e", "f", "f", "f"]
dic2 = Counter(arr2)
dic3 = sorted(dic2.items(), key = lambda x: (x[1], x[0]) )
# the key here for how we want to sort is a lambda function
# lambda function created for this sorted function only
# we take x which will be tuple and first sort on the value
# the count of the elements is the value
# then we sort on the key of the counter which will be the letter

print(dic2)
print(dic3)