import math
class Figure:
    sides_count = 0
    filled = None
    sides_abc = []

    def __init__(self, __color, *__sides):
        self.__sides = __sides
        self.__color = __color
        self.__sides = list(__sides)
        if len(__sides) == 1:
            self.__sides = [__sides[0]] * self.sides_count
            self.sides_abc = [__sides[0]] * self.sides_count
        else:
            for i in range(self.sides_count):
                list(__sides).append(1)

    def get_color(self):
        print(self.__color)

    def _is_valid_color(self, r, g, b):
        range_ = range(0, 255)
        if r in range_ and g in range_ and b in range_:
            return True

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def _is_valid_sides(self, **sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if isinstance(i, int):
                    return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.sides_abc)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
            self.sides_abc = new_sides


class Circle(Figure):
    sides_count = 1
    radius = 0
    def __init__(self, __color, *__sides):
        Figure.__init__(self, __color, __sides)
        side_int = __sides[0]
        self.radius = 6.28 / side_int

    def get_square(self):
        print(3.14*self.radius**2)


class Triangle(Figure):
    sides_count = 3


    def __init__(self, __color, *__sides):
        Figure.__init__(self, __color, *__sides)


    def get_square(self):
        semip = self.__len__()/2
        square = math.sqrt(semip*((semip - self.sides_abc[0]) * (semip - self.sides_abc[1]) * (semip - self.sides_abc[2])))
        print(square)


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __sides):
        Figure.__init__(self, __color, __sides)


    def get_volume(self):
        return self.sides_abc[0]**3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
