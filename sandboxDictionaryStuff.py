# doing some dictionary stuff
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "h", "a", "c", "c", "c"]

from collections import Counter
dic = Counter(letters)
print(dic)
print("a" in dic)
for key, value in dic.items():
    print("key is:", key, " value is: ", value)