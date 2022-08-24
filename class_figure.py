class Rectangle:
    def __init__(self, height: int, widght: int, sqare: int):
        self.widght = widght
        self.height = height

    def area(self):
        return self.widght * self.height

r1 = Rectangle(15, 43)
print(r1.area())



class Circle:
    def __init__(self, rad: int):
        self.rad = rad
