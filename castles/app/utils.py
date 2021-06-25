# -*- coding: utf-8 -*-
import pygame

G_ACC = 9.81


def load_image(filename):
    return pygame.image.load(filename).convert_alpha()


def crop(minimum, elem, maximum):
    return max(minimum, min(maximum, elem))
