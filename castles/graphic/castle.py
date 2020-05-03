# -*- coding: utf-8 -*-
from app.utils import Colour, Vector2D
from graphic.graphics import GROUND_COLOUR


class CastleGraphic:
    _ACTIVE_COLOUR = Colour(48, 48, 48)
    _INACTIVE_COLOUR = Colour(128, 128, 128)

    def __init__(self, graphics, castle):
        self._graphics = graphics
        self._castle = castle

    def draw_active_sign(self):
        self._draw_sign_shape(self._ACTIVE_COLOUR)

    def draw_inactive_sign(self):
        self._draw_sign_shape(self._INACTIVE_COLOUR)

    def erase_sign(self):
        self._draw_sign_shape(GROUND_COLOUR)

    def draw_info(self):
        self._graphics.text(f"LIFE:   {self._castle.life}", Vector2D(10, 10))
        self._graphics.text(f"ANGLE:  {self._castle.cannon.angle}", Vector2D(10, 40))
        self._graphics.text(f"SPEED:  {self._castle.speed}", Vector2D(10, 70))

    def _draw_sign_shape(self, colour):
        pos = self._castle.position + (10, 24)

        for diff in range(7):
            self._graphics.line(pos + Vector2D(diff, 6), pos + Vector2D(diff, diff), tuple(colour))
            self._graphics.line(pos + Vector2D(-diff, 6), pos + Vector2D(-diff, diff),
                                tuple(colour))
