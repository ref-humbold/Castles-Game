# -*- coding: utf-8 -*-
import pygame

from graphic.graphics import Background, Graphics


class Game:
    def __init__(self):
        self.players = []
        self._graphics = Graphics()
        self._playing = False

    def start(self):
        background = Background(self._graphics)
        background.draw()
        self._playing = True

    def play(self):
        self.start()

        while self._playing:
            for event in pygame.event.get():
                self._graphics.update()

                if event.type == pygame.QUIT:
                    self.end()
                    return

    def end(self):
        self._playing = False
