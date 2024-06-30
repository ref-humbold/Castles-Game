# -*- coding: utf-8 -*-
from random import randint

import pygame

from graphics.graphics import Graphics
from utils.colors import GROUND_COLOR, HEAVEN_COLOR
from utils.utils import crop


class Background:
    _UNIT_DIVISOR = 8
    _STEP_DIVISOR = 64

    def __init__(self, graphics: Graphics):
        self._graphics = graphics
        self.heights = []

    def draw(self):
        self._graphics.screen.fill(HEAVEN_COLOR)
        self._create()

        for x, height in enumerate(self.heights):
            self._graphics.line(pygame.Vector2(x, self._graphics.WINDOW_Y_SIZE),
                                pygame.Vector2(x, height),
                                GROUND_COLOR)

        self._graphics.update()

    def _create(self):
        unit = self._graphics.WINDOW_Y_SIZE // self._UNIT_DIVISOR
        min_height = 2 * unit
        max_height = (self._UNIT_DIVISOR - 1) * unit
        drawing_step = self._graphics.WINDOW_X_SIZE // self._STEP_DIVISOR
        max_diff = self._UNIT_DIVISOR - 1
        current_height = randint(min_height + unit, max_height - unit)

        for _ in range(0, self._graphics.WINDOW_X_SIZE, drawing_step):
            diff = randint(-max_diff, max_diff)

            for _ in range(1, drawing_step + 1):
                current_height = crop(min_height, current_height + diff, max_height)
                self.heights.append(current_height)
