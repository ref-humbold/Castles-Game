# -*- coding: utf-8 -*-
from math import cos, radians, tan

import pygame

from .graphics import HEAVEN_COLOUR
from .utils import Colour, G_ACC, Vector2D, bound


class Cannon:
    _IMAGE = pygame.image.load("images/cannon.jpg").convert()

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


class CannonBallGraphic:
    _COLOUR = Colour(0, 0, 0)
    _HALF_SIZE = 2

    def __init__(self, screen, castle):
        self._screen = screen
        self._is_vertical = castle.angle == 90
        self._angle = radians(castle.angle)
        self._speed = castle.speed
        self._start_pos = castle.cannon.muzzle
        self._current_pos = Vector2D(self._start_pos.x, self._start_pos.y)

    def throw(self):
        if self._is_vertical:
            # Vertical throw
            hmax_diff = self._speed * self._speed / (2 * G_ACC)
            hmax = max(0, self._start_pos.y - int(hmax_diff))

            while self._current_pos.y > hmax:
                self._draw()
                self._current_pos -= (0, 2)

            while self._current_pos.y < self._start_pos.y:
                self._current_pos += (0, 2)
                self._draw()
        else:
            # Parabolic throw
            while 0 < self._current_pos.x < self._screen.get_size()[0]:
                if self._current_pos.y >= 0:
                    self._draw()

                x_pos = self._current_pos.x + 2
                x_speed = self._speed * cos(self._angle)
                y_diff = x_pos * tan(self._angle) - G_ACC * x_pos * x_pos / (2 * x_speed * x_speed)
                y_pos = self._start_pos.y - int(y_diff)
                self._current_pos = Vector2D(x_pos, y_pos)

    def _draw(self):
        self._draw_shape(self._COLOUR)
        pygame.display.update()
        pygame.time.delay(50)
        self._draw_shape(HEAVEN_COLOUR)
        pygame.display.update()

    def _draw_shape(self, colour):
        for dx in range(-self._HALF_SIZE, self._HALF_SIZE):
            pygame.draw.line(self._screen,
                             colour.tuple,
                             (self._current_pos.x + dx, self._current_pos.y - self._HALF_SIZE),
                             (self._current_pos.x + dx, self._current_pos.y + self._HALF_SIZE))
