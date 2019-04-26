# -*- coding: utf-8 -*-

from random import randint

import pygame

from .utils import bound

HEAVEN_COLOUR = (0, 127, 255)
GROUND_COLOUR = (255, 255, 0)


class Background:
    """Klasa odpowiadająca za grafikę tła gry."""

    def __init__(self, screen):
        self._screen = screen
        self._heights = []
        self._font = pygame.font.SysFont("arial", 24)
        self._angle_label = self._render_value("ANGLE: ")
        self._speed_label = self._render_value("SPEED: ")

    def draw(self):
        """Rysuje tło do gry."""
        self._screen.fill(HEAVEN_COLOUR)
        self._create()

        for x_pos, height in enumerate(self._heights):
            pygame.draw.line(self._screen, GROUND_COLOUR,
                             (x_pos, 640), (x_pos, height))

        self._blit_labels(0, 20)

    def _create(self):
        """Ustawia wysokości na tle."""
        current_height = randint(320, 560)

        for _ in range(0, 1024, 16):
            diff = randint(-4, 4)

            for column in range(1, 17):
                current_height = bound(54, current_height + column * diff, 586)
                self._heights.append(current_height)

    def _blit_labels(self, angle, speed):
        """Wyświetla etykiety na ekranie
        :param angle: wartość kąta
        :param speed: wartość prędkości"""
        self._screen.blit(self._angle_label, (10, 10))
        self._screen.blit(self._speed_label, (10, 40))
        self._screen.blit(self._render_value(angle), (110, 10))
        self._screen.blit(self._render_value(speed), (110, 40))

    def _render_value(self, value):
        return self._font.render(str(value), 0, (0, 0, 0))
