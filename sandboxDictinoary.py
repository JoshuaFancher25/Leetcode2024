# playing with dictionaries

dic = {}
arr = [1,1,3,3,2,2,2,2]

for num in arr:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

print(dic)

# using the get method
# retrieve the current value associated with the num, if doesn't exist we can use a default value
# then we want to increment the value
dic2 = {}
for num in arr:
    dic2[num] = dic2.get(num, 0) + 1
print(dic2)
