# -*- coding: utf-8 -*-

from abc import ABCMeta

import pygame


# import dbm.ndbm


class Player(metaclass=ABCMeta):
    """Klasa odpowiadająca za pojedynczego gracza"""
    _ACTIVE_MARKER = (128, 128, 128)
    _INACTIVE_MARKER = (48, 48, 48)

    def __init__(self, number, image):
        self.number = str(number)
        self.castles = []
        self.castle_img = pygame.image.load(image).convert()


class HumanPlayer(Player):
    def __init__(self, number, image):
        super().__init__(number, image)


class CompPlayer(Player):
    def __init__(self, number, image):
        super().__init__(number, image)
