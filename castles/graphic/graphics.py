# -*- coding: utf-8 -*-
from random import randint

import pygame

from app.utils import crop

HEAVEN_COLOR = pygame.Color(0, 127, 255)
GROUND_COLOR = pygame.Color(255, 255, 0)


class Graphics:
    WINDOW_X_SIZE = 1024
    WINDOW_Y_SIZE = 640

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(self.WINDOW_X_SIZE, self.WINDOW_Y_SIZE))
        self.font = pygame.font.SysFont("arial", 24)
        pygame.display.set_caption("CASTLES GAME")

    def line(self, from_pos: pygame.Vector2, to_pos: pygame.Vector2, color: pygame.Color = None):
        if color is None:
            color = pygame.Color(0, 0, 0)

        pygame.draw.line(self.screen, color, from_pos, to_pos)

    def text(self, value: str, position: pygame.Vector2, color: pygame.Color = None):
        if color is None:
            color = pygame.Color(0, 0, 0)

        rendered_text = self.font.render(value, False, color)
        self.screen.blit(rendered_text, position)

    @staticmethod
    def update(delay: int = 0):
        pygame.display.update()

        if delay > 0:
            pygame.time.delay(delay)


class Background:
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

    def _create(self):
        current_height = randint(self._graphics.WINDOW_Y_SIZE // 2,
                                 7 * self._graphics.WINDOW_Y_SIZE // 8)

        for _ in range(0, self._graphics.WINDOW_X_SIZE, 16):
            diff = randint(-4, 4)

            for column in range(1, 17):
                current_height = crop(54, current_height + column * diff, 586)
                self._heights.append(current_height)
