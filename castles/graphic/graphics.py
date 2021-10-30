# -*- coding: utf-8 -*-
from random import randint

import pygame

from app.utils import crop

HEAVEN_COLOR = pygame.Color(0, 127, 255)
GROUND_COLOR = pygame.Color(255, 255, 0)
BASIC_COLOR = pygame.Color(0, 0, 0)


class Graphics:
    WINDOW_X_SIZE = 1600
    WINDOW_Y_SIZE = 900

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(self.WINDOW_X_SIZE, self.WINDOW_Y_SIZE))
        self.font = pygame.font.SysFont("arial", 24)
        pygame.display.set_caption("CASTLES GAME")

    def line(self, start: pygame.Vector2, end: pygame.Vector2, color: pygame.Color = BASIC_COLOR):
        pygame.draw.line(self.screen, color, start, end)

    def text(self, value: str, position: pygame.Vector2, color: pygame.Color = BASIC_COLOR):
        rendered_text = self.font.render(value, False, color)
        self.screen.blit(rendered_text, position)

    @staticmethod
    def update(delay: int = 0):
        pygame.display.update()

        if delay > 0:
            pygame.time.delay(delay)


class Background:
    _UNIT_DIVISOR = 8
    _STEP_DIVISOR = 64

    def __init__(self, graphics: Graphics):
        self._graphics = graphics
        self._heights = []

    def draw(self):
        self._graphics.screen.fill(HEAVEN_COLOR)
        self._create()

        for x, height in enumerate(self._heights):
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
                self._heights.append(current_height)
