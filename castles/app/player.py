# -*- coding: utf-8 -*-
from abc import ABCMeta

from app.utils import load_image


class Player(metaclass=ABCMeta):
    def __init__(self, number: int, image_name: str):
        self._image = load_image(image_name)
        self.number = str(number)
        self.castles = []


class HumanPlayer(Player):
    def __init__(self, number: int, image_name: str):
        super().__init__(number, image_name)


class CompPlayer(Player):
    def __init__(self, number: int, image_name: str):
        super().__init__(number, image_name)
