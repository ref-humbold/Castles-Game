# -*- coding: utf-8 -*-
import pygame

from app.utils import Vector2D, bound, load_image


class Cannon:
    _BASE_IMAGE = load_image("images/cannon.jpg")

    def __init__(self, x, y):
        self.position = Vector2D(x, y)
        self.angle = 0.0
        self._image = self._BASE_IMAGE

    @property
    def muzzle(self):
        if self.angle == 0.0:
            return self.position + Vector2D(self._image.get_size()[0], 0)

        if self.angle == 90.0:
            return self.position + Vector2D(0, self._image.get_size()[1])

        if self.angle == 180.0:
            return self.position - Vector2D(self._image.get_size()[0], 0)

        if self.angle < 90.0:
            return self.position + Vector2D(*self._image.get_size())

        return self.position - Vector2D(*self._image.get_size())

    def change_angle(self, diff):
        self.angle = bound(0.0, self.angle + diff, 180.0)
        self._image = pygame.transform.rotate(self._BASE_IMAGE, self.angle)
