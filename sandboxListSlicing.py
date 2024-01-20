
# practice with list slicing

word = "Hello World"
print(word[1:])
print(word[::-1])
print(word)
print(word[1:2])
emptyword = [""]
print(len(emptyword))
# class a blueprint for object creation
# object - models real world objects in code
# classes are very cool and fundamental in OOP (object oriented programming)
class Something:
    def stuff(self, x):
        print(x)
x = Something()
# must create an instance of the class
x.stuff("print this")