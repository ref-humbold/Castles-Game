# -*- coding: utf-8 -*-


class Pos:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def tuple(self):
        return self.x, self.y


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
