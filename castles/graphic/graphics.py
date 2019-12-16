# -*- coding: utf-8 -*-
from random import randint

import pygame

from app.utils import Colour, Vector2D, bound

HEAVEN_COLOUR = Colour(0, 127, 255)
GROUND_COLOUR = Colour(255, 255, 0)


def load_image(filename):
    pygame.image.load(filename).convert()


class Graphics:
    X_SIZE = 1024
    Y_SIZE = 640

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.X_SIZE, self.Y_SIZE))
        self.font = pygame.font.SysFont("arial", 24)
        pygame.display.set_caption("GRA W ZAMKI")

    def update(self, delay=0):
        pygame.display.update()

        if delay > 0:
            pygame.time.delay(delay)

    def line(self, from_pos, to_pos, colour=None):
        if colour is None:
            colour = Colour(0, 0, 0)

        pygame.draw.line(self.screen, colour.tuple, from_pos.tuple, to_pos.tuple)

    def text(self, value, position, colour=None):
        if colour is None:
            colour = Colour(0, 0, 0)

        txt = self.font.render(str(value), 0, colour)
        self.screen.blit(txt, position)


class Background:
    def __init__(self, graphics):
        self._graphics = graphics
        self._heights = []
        self._angle_label = "ANGLE: "
        self._speed_label = "SPEED: "

    def draw(self):
        self._graphics.screen.fill(HEAVEN_COLOUR.tuple)
        self._create()

        for x_pos, height in enumerate(self._heights):
            self._graphics.line(Vector2D(x_pos, self._graphics.Y_SIZE), Vector2D(x_pos, height),
                                GROUND_COLOUR.tuple)

        self._draw_labels(0, 20)

    def _create(self):
        current_height = randint(self._graphics.Y_SIZE // 2, 7 * self._graphics.Y_SIZE // 8)

        for _ in range(0, self._graphics.X_SIZE, 16):
            diff = randint(-4, 4)

            for column in range(1, 17):
                current_height = bound(54, current_height + column * diff, 586)
                self._heights.append(current_height)

    def _draw_labels(self, angle, speed):
        self._graphics.text(self._angle_label, Vector2D(10, 10))
        self._graphics.text(self._speed_label, Vector2D(10, 40))
        self._graphics.text(angle, Vector2D(110, 10))
        self._graphics.text(speed, Vector2D(110, 40))
