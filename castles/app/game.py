# -*- coding: utf-8 -*-
import pygame

from graphics.background import Background
from graphics.graphics import Graphics


class Game:
    def __init__(self):
        self.players = []
        self._graphics = Graphics()

    def play(self):
        self._start()
        self._run()
        self._end()

    def _start(self):
        background = Background(self._graphics)
        background.draw()

    def _run(self):

        while True:
            for event in pygame.event.get():
                self._graphics.update()

                if event.type == pygame.QUIT:
                    return

    def _end(self):
        self._graphics.quit()
        pygame.quit()
