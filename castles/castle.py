# -*- coding: utf-8 -*-
import pygame

from .cannon import Cannon
from .graphics import GROUND_COLOUR
from .utils import Vector2D, bound


class Castle:
    def __init__(self, x_pos, y_pos, image):
        self.position = Vector2D(x_pos, y_pos)
        self.image = image
        self.actual = False
        self.life = 100
        self.speed = 20.0
        self.cannon = Cannon(self.position.x + self.image.get_size[0] // 2,
                             self.position.y + self.image.get_size[1] // 2)

    @property
    def angle(self):
        return self.cannon.angle

    def change_speed(self, diff):
        self.speed = bound(20.0, self.speed + diff, 3.0 * self.life + 100.0)

    def change_angle(self, diff):
        self.cannon.change_angle(diff)


class CastleGraphic:
    _ACTIVE_COLOUR = (48, 48, 48)
    _INACTIVE_COLOUR = (128, 128, 128)

    def __init__(self, screen, castle):
        self._screen = screen
        self.castle = castle

    def draw_active_sign(self):
        self._draw_sign_shape(self._ACTIVE_COLOUR)

    def draw_inactive_sign(self):
        self._draw_sign_shape(self._INACTIVE_COLOUR)

    def erase_sign(self):
        self._draw_sign_shape(GROUND_COLOUR)

    def _draw_sign_shape(self, colour):
        x_pos = self.castle.position[0] + 10
        y_pos = self.castle.position[1] + 24

        for diff in range(7):
            pygame.draw.line(self._screen, colour, (x_pos + diff, y_pos + 6),
                             (x_pos + diff, y_pos + diff))
            pygame.draw.line(self._screen, colour, (x_pos - diff, y_pos + 6),
                             (x_pos - diff, y_pos + diff))
