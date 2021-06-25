# -*- coding: utf-8 -*-
import pygame

from app.cannon import Cannon
from app.utils import crop


class Castle:
    def __init__(self, x, y, image):
        self.position = pygame.Vector2(x, y)
        self.image = image
        self.life = 100
        self.speed = 20.0
        self.cannon = Cannon(self.position.x + self.image.get_width() // 2,
                             self.position.y + self.image.get_height() // 2)

    @property
    def angle(self):
        return self.cannon.angle

    def change_speed(self, diff):
        self.speed = crop(20.0, self.speed + diff, 3.0 * self.life + 100.0)

    def change_angle(self, diff):
        self.cannon.change_angle(diff)
