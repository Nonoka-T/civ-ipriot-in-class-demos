from animal import Animal

class Duck(Animal):
    def __init__(self, size, weight, colour, is_wet):
        super().__init__(size, weight, colour)
        self.is_wet = is_wet

    def move(self):
        print("It's waddling!")

class Door:
    def move(self):
        print("it opens, creeeak")

if __name__ == "__main__":
    animal = Animal("big", "largel", "grey")
    animal.sleep()
    duck = Duck("small", "light", "brown", True)
    duck.sleep()
    door = Door()

    for thing in [animal, duck, door]:
        thing.move()