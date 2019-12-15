# -*- coding: utf-8 -*-

G_ACC = 9.81


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def tuple(self):
        return self.x, self.y

    def __iadd__(self, other):
        if type(other) == Vector2D:
            other = other.tuple

        self.x += other[0]
        self.y += other[1]

    def __add__(self, other):
        if type(other) == Vector2D:
            other = other.tuple

        return Vector2D(self.x + other[0], self.y + other[1])

    def __isub__(self, other):
        if type(other) == Vector2D:
            other = other.tuple

        self.x -= other[0]
        self.y -= other[1]

    def __sub__(self, other):
        if type(other) == Vector2D:
            other = other.tuple

        return Vector2D(self.x - other[0], self.y - other[1])


class Colour:
    def __init__(self, r=0, g=0, b=0):
        self._r = r
        self._g = g
        self._b = b

    @property
    def tuple(self):
        return self._r, self._g, self._b


def bound(minimum, elem, maximum):
    return minimum if elem < minimum else maximum if elem > maximum else elem
