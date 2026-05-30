class shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        pass

class triangle(shape):
    def __init__(self, width, length):
        super().__init__(width, length)
        self.width = width
        self.length = length
    def area(self):
        area = 0.5*(self.length* self.width)
        return area

class square(shape):
    def __init__(self, width, length):
        super().__init__(width, length)
        self.width = width
        self.length = length
    def area(self):
        area = self.length* self.width
        return area
    
triangle = triangle(5, 10)
print("Area of triangle: ", triangle.area())
square = square(5, 10)
print("Area of triangle: ", square.area())