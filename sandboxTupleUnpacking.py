# learning tuple unpacking
a = (1,2,3,4,5)
b, c, d, e, f = a
print(b)
x, *y = a
print(type(y))
print(type(a))
g = list(a)
print(g)
print(type(g))
x = [0 * 10]
print(x)