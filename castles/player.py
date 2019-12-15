# -*- coding: utf-8 -*-
from abc import ABCMeta

import pygame


class Player(metaclass=ABCMeta):
    _ACTIVE_MARKER = (128, 128, 128)
    _INACTIVE_MARKER = (48, 48, 48)

    def __init__(self, number, image):
        castle_img = pygame.image.load(image).convert()
        self.number = str(number)
        self.castles = []


class HumanPlayer(Player):
    def __init__(self, number, image):
        super().__init__(number, image)


class CompPlayer(Player):
    def __init__(self, number, image):
        super().__init__(number, image)
