# -*- coding: utf-8 -*-
import pygame

from app.castle import Castle
from graphic.graphics import GROUND_COLOR, Graphics


class CastleGraphic:
    _ACTIVE_COLOR = pygame.Color(48, 48, 48)
    _INACTIVE_COLOR = pygame.Color(128, 128, 128)
    _SIGN_SIZE = 6

    def __init__(self, graphics: Graphics, castle: Castle, image: pygame.Surface):
        self.castle = castle
        self.image = image
        self._graphics = graphics

    def draw_active_sign(self):
        self._draw_sign_shape(self._ACTIVE_COLOR)

    def draw_inactive_sign(self):
        self._draw_sign_shape(self._INACTIVE_COLOR)

    def erase_sign(self):
        self._draw_sign_shape(GROUND_COLOR)

    def draw_info(self):
        self._graphics.text(f"LIFE:   {self.castle.life}", pygame.Vector2(10, 10))
        self._graphics.text(f"ANGLE:  {self.castle.cannon.angle}", pygame.Vector2(10, 40))
        self._graphics.text(f"SPEED:  {self.castle.speed}", pygame.Vector2(10, 70))

    def _draw_sign_shape(self, color: pygame.Color):
        pos = self.castle.position + pygame.Vector2(0, 24)

        for diff in range(self._SIGN_SIZE + 1):
            self._graphics.line(pos + pygame.Vector2(diff, self._SIGN_SIZE),
                                pos + pygame.Vector2(diff, diff),
                                color)
            self._graphics.line(pos + pygame.Vector2(-diff, self._SIGN_SIZE),
                                pos + pygame.Vector2(-diff, diff),
                                color)
