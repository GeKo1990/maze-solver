from window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, x1: int, x2: int, y1: int, y2: int, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right), "black")