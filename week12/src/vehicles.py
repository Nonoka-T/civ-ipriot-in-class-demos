class Vehicle:
    def __init__(self, kind):
        self.__kind = kind # "Private"

    def kind(self):
        print(self.__kind)

    def move(self):
        raise RuntimeError("Vehicles are abstract and should be implemented")

class Boat(Vehicle):
    def __init__(self):
        super().__init__("Boat")

    def move(self):
        print("🌊")

class Train(Vehicle):
    def __init__(self):
        super().__init__("Train")

    def move(self):
        print("🚂 choo-choo!")

class Cat():
    def move(self):
        print("pitter patter meow")


if __name__ == "__main__":
    train = Train()
    boat = Boat()
    cat = Cat()

    for thing in [cat, boat, train]:
        thing.move()



