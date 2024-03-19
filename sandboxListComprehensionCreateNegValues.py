# learning more list comprehension

arr = [0,1,1,3,0,5]
newarr = [i for i in arr if i > 0]
print(newarr)

anotherarr = [i*-1 for i in arr]
print(anotherarr)