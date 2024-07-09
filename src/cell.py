import math

from window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, x1: int, x2: int, y1: int, y2: int, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
        self.visited = False

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if not self._win:
            return

        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left), "black")
        else:
            self._win.draw_line(Line(top_left, bottom_left), "#d9d9d9")
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), "black")
        else:
            self._win.draw_line(Line(top_left, top_right), "#d9d9d9")
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right), "black")
        else:
            self._win.draw_line(Line(top_right, bottom_right), "#d9d9d9")
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right), "black")
        else:
            self._win.draw_line(Line(bottom_left, bottom_right), "#d9d9d9")

    def center(self):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return (center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if not undo:
            color = "red"
        
        start = Point(self.center()[0], self.center()[1])
        end = Point(to_cell.center()[0], to_cell.center()[1])
        self._win.draw_line(Line(start, end), color)