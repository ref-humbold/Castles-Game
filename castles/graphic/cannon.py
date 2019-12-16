from math import cos, radians, tan

from app.utils import Colour, G_ACC, Vector2D
from graphic.graphics import HEAVEN_COLOUR


class CannonBallGraphic:
    _COLOUR = Colour(0, 0, 0)
    _HALF_SIZE = 2

    def __init__(self, graphics, castle):
        self._graphics = graphics
        self._is_vertical = castle.angle == 90
        self._angle = radians(castle.angle)
        self._speed = castle.speed
        self._start_pos = castle.cannon.muzzle
        self._current_pos = Vector2D(self._start_pos.x, self._start_pos.y)

    def throw(self):
        if self._is_vertical:
            # Vertical throw
            hmax_diff = self._speed * self._speed / (2 * G_ACC)
            hmax = max(0, self._start_pos.y - int(hmax_diff))

            while self._current_pos.y > hmax:
                self._draw()
                self._current_pos -= (0, 2)

            while self._current_pos.y < self._start_pos.y:
                self._current_pos += (0, 2)
                self._draw()
        else:
            # Parabolic throw
            while 0 < self._current_pos.x < self._graphics.screen.get_size()[0]:
                if self._current_pos.y >= 0:
                    self._draw()

                x_pos = self._current_pos.x + 2
                x_speed = self._speed * cos(self._angle)
                y_diff = x_pos * tan(self._angle) - G_ACC * x_pos * x_pos / (2 * x_speed * x_speed)
                y_pos = self._start_pos.y - int(y_diff)
                self._current_pos = Vector2D(x_pos, y_pos)

    def _draw(self):
        self._draw_shape(self._COLOUR)
        self._graphics.update(50)
        self._draw_shape(HEAVEN_COLOUR)
        self._graphics.update()

    def _draw_shape(self, colour):
        for dx in range(-self._HALF_SIZE, self._HALF_SIZE):
            self._graphics.line(self._current_pos + (dx, -self._HALF_SIZE),
                                self._current_pos + (dx, self._HALF_SIZE),
                                colour.tuple)
