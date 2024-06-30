# -*- coding: utf-8 -*-
import pygame

from utils.colors import BASIC_COLOR


class Graphics:
    PYGAME_MODULES = [pygame.display, pygame.font]
    WINDOW_X_SIZE = 1600
    WINDOW_Y_SIZE = 900

    def __init__(self):
        self.init()
        self.screen = pygame.display.set_mode(size=(self.WINDOW_X_SIZE, self.WINDOW_Y_SIZE))
        self.font = pygame.font.SysFont("arial", 24)
        pygame.display.set_caption("CASTLES GAME")

    def line(self, start: pygame.Vector2, end: pygame.Vector2, color: pygame.Color = BASIC_COLOR):
        pygame.draw.line(self.screen, color, start, end)

    def text(self, value: str, position: pygame.Vector2, color: pygame.Color = BASIC_COLOR):
        rendered_text = self.font.render(value, False, color)
        self.screen.blit(rendered_text, position)

    @classmethod
    def init(cls):
        for module in cls.PYGAME_MODULES:
            module.init()

    @classmethod
    def quit(cls):
        for module in reversed(cls.PYGAME_MODULES):
            module.quit()

    @staticmethod
    def update(delay: int = 0):
        pygame.display.update()

        if delay > 0:
            pygame.time.delay(delay)
