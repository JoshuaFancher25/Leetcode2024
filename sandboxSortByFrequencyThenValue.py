# sorting by frequency and then by value

arr = [1,1,1,1,3,3,3,2,2,5,5,7,7,7,7,7]
from collections import Counter

dic = Counter(arr)
print(dic)
newdic = (sorted(dic.items(), key= lambda x:(x[1], x[0]), reverse = True))
# somewhat like sql in how we specify the sorting order
# first we sort by element 1 then by element 0
# the elements are extracted from the x which is an iterable in dic.items()
# the x itself it a tuple form dic.items and it has two values

print(newdic)