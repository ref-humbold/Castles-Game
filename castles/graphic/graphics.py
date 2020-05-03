# -*- coding: utf-8 -*-
from random import randint

import pygame

from app.utils import Colour, Vector2D, bound

HEAVEN_COLOUR = Colour(0, 127, 255)
GROUND_COLOUR = Colour(255, 255, 0)


class Graphics:
    WINDOW_X_SIZE = 1024
    WINDOW_Y_SIZE = 640

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WINDOW_X_SIZE, self.WINDOW_Y_SIZE))
        self.font = pygame.font.SysFont("arial", 24)
        pygame.display.set_caption("CASTLES GAME")

    def update(self, delay=0):
        pygame.display.update()

        if delay > 0:
            pygame.time.delay(delay)

    def line(self, from_pos, to_pos, colour=None):
        if colour is None:
            colour = Colour(0, 0, 0)

        pygame.draw.line(self.screen, tuple(colour), tuple(from_pos), tuple(to_pos))

    def text(self, value, position, colour=None):
        if colour is None:
            colour = Colour(0, 0, 0)

        rendered_text = self.font.render(str(value), 0, colour)
        self.screen.blit(rendered_text, position)


class Background:
    def __init__(self, graphics):
        self._graphics = graphics
        self._heights = []

    def draw(self):
        self._graphics.screen.fill(tuple(HEAVEN_COLOUR))
        self._create()

        for x, height in enumerate(self._heights):
            self._graphics.line(Vector2D(x, self._graphics.WINDOW_Y_SIZE),
                                Vector2D(x, height),
                                tuple(GROUND_COLOUR))

    def _create(self):
        current_height = randint(self._graphics.WINDOW_Y_SIZE // 2,
                                 7 * self._graphics.WINDOW_Y_SIZE // 8)

        for _ in range(0, self._graphics.WINDOW_X_SIZE, 16):
            diff = randint(-4, 4)

            for column in range(1, 17):
                current_height = bound(54, current_height + column * diff, 586)
                self._heights.append(current_height)
