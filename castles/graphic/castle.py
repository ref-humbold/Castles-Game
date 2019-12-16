# -*- coding: utf-8 -*-
from app.utils import Colour
from graphic.graphics import GROUND_COLOUR


class CastleGraphic:
    _ACTIVE_COLOUR = Colour(48, 48, 48)
    _INACTIVE_COLOUR = Colour(128, 128, 128)

    def __init__(self, graphics, castle):
        self._graphics = graphics
        self.castle = castle

    def draw_active_sign(self):
        self._draw_sign_shape(self._ACTIVE_COLOUR)

    def draw_inactive_sign(self):
        self._draw_sign_shape(self._INACTIVE_COLOUR)

    def erase_sign(self):
        self._draw_sign_shape(GROUND_COLOUR)

    def _draw_sign_shape(self, colour):
        pos = self.castle.position + (10, 24)

        for diff in range(7):
            self._graphics.line(pos + (diff, 6), pos + (diff, diff), colour.tuple)
            self._graphics.line(pos + (-diff, 6), pos + (-diff, diff), colour.tuple)
