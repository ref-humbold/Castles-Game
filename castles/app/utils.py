# -*- coding: utf-8 -*-
from typing import TypeVar

import pygame

G_ACC = 9.81

_T = TypeVar("_T")


def load_image(filename: str) -> pygame.Surface:
    return pygame.image.load(filename).convert_alpha()


def crop(minimum: _T, elem: _T, maximum: _T) -> _T:
    return max(minimum, min(maximum, elem))
