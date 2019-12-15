# -*- coding: utf-8 -*-

import pygame


class Game:
    X_SIZE = 1024
    Y_SIZE = 640

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self.X_SIZE, self.Y_SIZE))
        pygame.display.set_caption("GRA W ZAMKI")

    @property
    def screen(self):
        return self._screen
