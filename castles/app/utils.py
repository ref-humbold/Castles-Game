# -*- coding: utf-8 -*-
import pygame

G_ACC = 9.81


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)


class Colour:
    def __init__(self, r=0, g=0, b=0):
        self._r = r
        self._g = g
        self._b = b

    def __iter__(self):
        yield self._r
        yield self._g
        yield self._b


def load_image(filename):
    pygame.image.load(filename).convert()


def bound(minimum, elem, maximum):
    return minimum if elem < minimum else maximum if elem > maximum else elem
