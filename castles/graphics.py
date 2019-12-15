# -*- coding: utf-8 -*-
from random import randint

import pygame

from .utils import Colour, bound

HEAVEN_COLOUR = Colour(0, 127, 255)
GROUND_COLOUR = Colour(255, 255, 0)


class Background:
    def __init__(self, game):
        self._game = game
        self._heights = []
        self._font = pygame.font.SysFont("arial", 24)
        self._angle_label = self._render_value("ANGLE: ")
        self._speed_label = self._render_value("SPEED: ")

    def draw(self):
        self._game.screen.fill(HEAVEN_COLOUR.tuple)
        self._create()

        for x_pos, height in enumerate(self._heights):
            pygame.draw.line(self._game.screen, GROUND_COLOUR.tuple, (x_pos, self._game.Y_SIZE),
                             (x_pos, height))

        self._blit_labels(0, 20)

    def _create(self):
        current_height = randint(self._game.Y_SIZE // 2, 7 * self._game.Y_SIZE // 8)

        for _ in range(0, self._game.X_SIZE, 16):
            diff = randint(-4, 4)

            for column in range(1, 17):
                current_height = bound(54, current_height + column * diff, 586)
                self._heights.append(current_height)

    def _blit_labels(self, angle, speed):
        self._game.screen.blit(self._angle_label, (10, 10))
        self._game.screen.blit(self._speed_label, (10, 40))
        self._game.screen.blit(self._render_value(angle), (110, 10))
        self._game.screen.blit(self._render_value(speed), (110, 40))

    def _render_value(self, value):
        return self._font.render(str(value), 0, (0, 0, 0))
