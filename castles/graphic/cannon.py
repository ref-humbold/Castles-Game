# -*- coding: utf-8 -*-
from math import cos, radians, tan

import pygame

from app.utils import G_ACC
from graphic.graphics import HEAVEN_COLOR


class CannonBallGraphic:
    _COLOR = pygame.Color(0, 0, 0)
    _SIZE = 4

    def __init__(self, graphics, castle):
        self._graphics = graphics
        self._is_vertical = castle.angle == 90.0
        self._angle = radians(castle.angle)
        self._speed = castle.speed
        self._start_pos = castle.cannon.end
        self._current_pos = pygame.Vector2(self._start_pos.x, self._start_pos.y)

    def throw(self):
        if self._is_vertical:
            # Vertical throw
            max_height_diff = self._speed * self._speed / (2 * G_ACC)
            max_height = max(0, self._start_pos.y - int(max_height_diff))

            while self._current_pos.y > max_height:
                self._draw()
                self._current_pos -= pygame.Vector2(0, 2)

            while self._current_pos.y < self._start_pos.y:
                self._current_pos += pygame.Vector2(0, 2)
                self._draw()
        else:
            # Parabolic throw
            while 0 < self._current_pos.x < self._graphics.screen.get_width():
                if self._current_pos.y >= 0:
                    self._draw()

                x_pos = self._current_pos.x + 2
                x_speed = self._speed * cos(self._angle)
                y_diff = x_pos * tan(self._angle) - G_ACC * x_pos * x_pos / (2 * x_speed * x_speed)
                y_pos = self._start_pos.y - int(y_diff)
                self._current_pos = pygame.Vector2(x_pos, y_pos)

    def _draw(self):
        self._draw_shape(self._COLOR)
        self._graphics.update(50)
        self._draw_shape(HEAVEN_COLOR)
        self._graphics.update()

    def _draw_shape(self, color):
        half_size = self._SIZE // 2

        for dx in range(-half_size, half_size):
            self._graphics.line(self._current_pos + pygame.Vector2(dx, -half_size),
                                self._current_pos + pygame.Vector2(dx, half_size),
                                color)
