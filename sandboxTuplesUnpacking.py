# learning about more tuple unpacking

tup = (1,2,3,4,10)
a, *b = tup
print(a)
print(b)

elements = (10,11,12,13)
a,*z,b = elements
print(a)
print(b)
print(z)

# tuples are immutable objects in python
