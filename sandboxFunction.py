# how to define a function in python

def afunction(num1, num2):
    return num1 + num2


print(afunction(10, 15))


# defining a class
class Adder:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age


x = Adder("bob", "smith", 24)
print(x.fname)
print(x.age)
