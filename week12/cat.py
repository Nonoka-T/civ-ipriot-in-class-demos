class Cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        return f'meows'

# Cat.name
c = Cat("Lenny")
print(c.name)
d = Cat("Kenny")
print(c.name)
print(d.name)