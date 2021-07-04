# -*- coding: utf-8 -*-
import pygame

from app.utils import crop, load_image


class Cannon:
    _BASE_IMAGE = load_image("images/cannon.jpg")

    def __init__(self, x: float, y: float):
        self.position = pygame.Vector2(x, y)
        self.angle = 0.0
        self._image = self._BASE_IMAGE

    @property
    def end(self) -> pygame.Vector2:
        x, y = self._image.get_size()

        if self.angle == 0.0:
            vector = pygame.Vector2(x, 0)
        elif self.angle == 90.0:
            vector = pygame.Vector2(0, y)
        elif self.angle == 180.0:
            vector = pygame.Vector2(-x, 0)
        elif self.angle < 90.0:
            vector = pygame.Vector2(x, y)
        else:
            vector = pygame.Vector2(-x, y)

        return self.position + vector

    def change_angle(self, diff: float):
        self.angle = crop(0.0, self.angle + diff, 180.0)
        self._image = pygame.transform.rotate(self._BASE_IMAGE, self.angle)
