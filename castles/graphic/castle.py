# -*- coding: utf-8 -*-
import pygame

from graphic.graphics import GROUND_COLOR


class CastleGraphic:
    _ACTIVE_COLOR = pygame.Color(48, 48, 48)
    _INACTIVE_COLOR = pygame.Color(128, 128, 128)

    def __init__(self, graphics, castle):
        self._graphics = graphics
        self._castle = castle

    def draw_active_sign(self):
        self._draw_sign_shape(self._ACTIVE_COLOR)

    def draw_inactive_sign(self):
        self._draw_sign_shape(self._INACTIVE_COLOR)

    def erase_sign(self):
        self._draw_sign_shape(GROUND_COLOR)

    def draw_info(self):
        self._graphics.text(f"LIFE:   {self._castle.life}", pygame.Vector2(10, 10))
        self._graphics.text(f"ANGLE:  {self._castle.cannon.angle}", pygame.Vector2(10, 40))
        self._graphics.text(f"SPEED:  {self._castle.speed}", pygame.Vector2(10, 70))

    def _draw_sign_shape(self, color):
        pos = self._castle.position + pygame.Vector2(10, 24)

        for diff in range(7):
            self._graphics.line(pos + pygame.Vector2(diff, 6),
                                pos + pygame.Vector2(diff, diff),
                                color)
            self._graphics.line(pos + pygame.Vector2(-diff, 6),
                                pos + pygame.Vector2(-diff, diff),
                                color)
