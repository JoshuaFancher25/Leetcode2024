# giving the range function non-integers
# its not possible the range function only takes in integers

for i in range(5):
    print(i)
print("-----")

# range take (start,stop,interval)
# -1 for an interval in reverse
# arguments must be comma separated
#

for i in range(0,10,2):
    print("steps of 2: ", i)
print("----")
for i in range(10,-1, -1):
    print("couting down: ", i)


"""
for i in range(4.4):
    print(i)
"""

# note we don't have to worry about integer overflow in python
# integer objects can be of arbitrary length
