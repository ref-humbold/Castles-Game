# -*- coding: utf-8 -*-
from app.cannon import Cannon
from app.utils import Vector2D, bound


class Castle:
    def __init__(self, x_pos, y_pos, image):
        self.position = Vector2D(x_pos, y_pos)
        self.image = image
        self.actual = False
        self.life = 100
        self.speed = 20.0
        self.cannon = Cannon(self.position.x + self.image.get_size[0] // 2,
                             self.position.y + self.image.get_size[1] // 2)

    @property
    def angle(self):
        return self.cannon.angle

    def change_speed(self, diff):
        self.speed = bound(20.0, self.speed + diff, 3.0 * self.life + 100.0)

    def change_angle(self, diff):
        self.cannon.change_angle(diff)
