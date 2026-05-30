class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print("Ares of restangele is: ", area)

r1 = rectangle(102,45)
r1.area()