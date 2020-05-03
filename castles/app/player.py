# -*- coding: utf-8 -*-
from abc import ABCMeta

from app.utils import load_image


class Player(metaclass=ABCMeta):
    def __init__(self, number, image):
        self._image = load_image(image)
        self.number = str(number)
        self.castles = []


class HumanPlayer(Player):
    def __init__(self, number, image):
        super().__init__(number, image)


class CompPlayer(Player):
    def __init__(self, number, image):
        super().__init__(number, image)
