import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()  # порівнювання площ обох прямокутників

    def __add__(self, other):
        area = self.get_square() + other.get_square()  # площа, де self - площа 1, other - площа 2
        new_width = self.width  # ширина нового прямокутника = ширина першого прямокутника
        new_height = area / new_width  # площа прямокутника = ширина * висота
        return Rectangle(new_width, new_height)  # новий об’єкт Rectangle з обчисленими стороною та висотою

    def __mul__(self, n):
        area = self.get_square() * n  # площа нового прямокутника = стара площа * n
        new_width = self.width  # ширина старого прямокутника = новому
        new_height = area / new_width  # обчислюємо висоту нового прямокутника
        return Rectangle(new_width, new_height)  # Повертаємо новий об’єкт Rectangle

    def __str__(self):
        return f"Rectangle({self.width}, {self.height}, {self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("OK")