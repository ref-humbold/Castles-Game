# -*- coding: utf-8 -*-
import pygame

from graphic.graphics import Background, Graphics


class Game:
    def __init__(self):
        self._graphics = Graphics()
        self._playing = False

    def start(self):
        background = Background(self._graphics)
        background.draw()
        self._playing = True

        while self._playing:
            for event in pygame.event.get():
                self._graphics.update()

                if event.type == pygame.QUIT:
                    self.end_game()
                    break

    def end_game(self):
        self._playing = False
