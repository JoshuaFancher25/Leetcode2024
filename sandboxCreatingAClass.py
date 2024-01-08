class Aquarium:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def fishes(self, name: str):
        self.name = name
    def myname(self):
        print(self.name)


bowl = Aquarium("bob", 10)
bowl.myname()
