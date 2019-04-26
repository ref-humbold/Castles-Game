# -*- coding: utf-8 -*-

import pygame
from math import cos, radians, tan

from .graphics import HEAVEN_COLOUR
from .utils import bound


class Cannon:
    _IMAGE = pygame.image.load("images/armata.jpg").convert_alpha()

    def __init__(self, position):
        self._image = self._IMAGE
        self.position = (position[0] + 11, position[1] + 7)
        self.angle = 0.0

    @property
    def size(self):
        return self._image.get_size()

    def change_angle(self, diff):
        """Zmienia kąt armaty w zamku.
        :param diff: zmiana kąta"""
        self.angle = bound(0.0, self.angle + diff, 180.0)
        self._image = pygame.transform.rotate(self._IMAGE, self.angle)


class CannonBallGraphic:
    _COLOUR = (0, 0, 0)

    def __init__(self, screen, castle):
        self._screen = screen
        self._angle = castle.angle
        self._start_pos = (None, None)
        self._current_pos = [None, None]
        self._speed = castle.speed * 0.75 * abs(cos(radians(self._angle)))

    def move(self):
        if self._angle == 90:
            hmax = max(
                0, self._start_pos[1] - int(self._speed * self._speed / (2 * 9.81)))

            while self._current_pos[1] > hmax:
                self._draw()
                self._current_pos[1] -= 2

            while self._current_pos[1] + 2 < self._start_pos[1]:
                self._current_pos[1] += 2
                self._draw()
        else:
            while 0 < self._current_pos[0] < self._screen.get_size()[0]:
                if self._current_pos[1] >= 0:
                    self._draw()

                self._make_move()

    def __draw(self):
        self._draw_shape(self._COLOUR)
        pygame.display.update()
        pygame.time.delay(50)
        self._draw_shape(HEAVEN_COLOUR)
        pygame.display.update()

    def __draw_shape(self, colour):
        pygame.draw.line(self._screen, colour,
                         (self._current_pos[0] - 2, self._current_pos[1] - 2),
                         (self._current_pos[0] - 2, self._current_pos[1] + 2))
        pygame.draw.line(self._screen, colour,
                         (self._current_pos[0] - 1, self._current_pos[1] - 2),
                         (self._current_pos[0] - 1, self._current_pos[1] + 2))
        pygame.draw.line(self._screen, colour,
                         (self._current_pos[0], self._current_pos[1] - 2),
                         (self._current_pos[0], self._current_pos[1] + 2))
        pygame.draw.line(self._screen, colour,
                         (self._current_pos[0] + 1, self._current_pos[1] - 2),
                         (self._current_pos[0] + 1, self._current_pos[1] + 2))

    def __make_move(self):
        dirsign = 1 if self._angle < 90 else -1
        self._current_pos[0] += dirsign * 2
        self._current_pos[1] = self._parabola(self._current_pos[0])

    def __parabola(self, x_pos):
        y_diff = x_pos * tan(radians(self._angle)) \
                 - 9.81 * x_pos * x_pos / (2 * self._speed * self._speed)

        return self._start_pos[1] - int(y_diff)
