class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_circumference(self):
        return 2 * (self.height + self.width)

def main():
    print("AI to calculate attributes of rectangles!")
    height = int(input("Height? "))
    width = int(input("Width? "))
    r = Rectangle(height, width)
    print("The area of YOUR rectangle is:", r.get_area())
    print("The circumference of YOUR rectangle is:", r.get_circumference())

if __name__ == '__main__':
    main()