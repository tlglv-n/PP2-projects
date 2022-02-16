class shape:
    def area(self):
        return 0

class square(shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2


class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


get_square = square(int(input()))
print(get_square.area())

get_rectangle = rectangle(int(input()), int(input()))
print(get_rectangle.area())
