# -*- coding: utf-8 -*-
import pygame

from app.utils import Vector2D, bound
from graphic.graphics import load_image


class Cannon:
    _IMAGE = load_image("images/cannon.jpg")

    def __init__(self, x_pos, y_pos):
        self.position = Vector2D(x_pos, y_pos)
        self.angle = 0.0
        self._image = self._IMAGE

    @property
    def muzzle(self):
        if self.angle == 0.0:
            return self.position + (self._image.get_size()[0], 0)

        if self.angle == 90.0:
            return self.position + (0, self._image.get_size()[1])

        if self.angle == 180.0:
            return self.position - (self._image.get_size()[0], 0)

        if self.angle < 90.0:
            return self.position + self._image.get_size()

        return self.position - self._image.get_size()

    def change_angle(self, diff):
        self.angle = bound(0.0, self.angle + diff, 180.0)
        self._image = pygame.transform.rotate(self._IMAGE, self.angle)
