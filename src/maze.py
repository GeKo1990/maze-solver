import time
import random

from window import Window
from cell import Cell

class Maze:
    def __init__(
            self, x1, y1, num_rows: int, num_cols: int,
            cell_size_x: int, cell_size_y: int, win: Window = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        random.seed(1)
        self._create_cells()

    def _create_cells(self):
        for row_idx in range(self._num_rows):
            row = []
            for col_idx in range(self._num_cols):
                x1 = self._x1 + (col_idx * self._cell_size_x)
                x2 = self._x1 + ((col_idx + 1) * self._cell_size_x)
                y1 = self._y1 + (row_idx * self._cell_size_y)
                y2 = self._y1 + ((row_idx + 1) * self._cell_size_y)
                cell = Cell(x1, x2, y1, y2, self._win)
                row.append(cell)
                cell.draw()
            self._cells.append(row)            

        self._animate()

    def _animate(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        while(self._win):
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        end = self._cells[self._num_rows - 1][self._num_cols - 1]

        if random.choice([True, False]):
            start.has_right_wall = False
        else:
            start.has_bottom_wall = False
        start.draw()

        if random.choice([True, False]):
            end.has_left_wall = False
        else:
            end.has_top_wall = False
        end.draw()

    def _break_walls_r(self, x, y):
        current_cell = self._cells[x][y]
        current_cell.visited = True

        while True:
            possible_coords = []

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i == 0 and j != 0) or (i != 0 and j == 0):
                        p_x = x + i
                        p_y = y + j

                        if 0 <= p_x < self._num_rows and 0 <= p_y < self._num_cols:
                            possible_cell = self._cells[p_x][p_y]
                            if not possible_cell.visited:
                                if i == -1 and j == 0:
                                    possible_coords.append((p_x, p_y, "left"))
                                elif i == 1 and j == 0:
                                    possible_coords.append((p_x, p_y, "right"))
                                elif i == 0 and j == -1:
                                    possible_coords.append((p_x, p_y, "up"))
                                elif i == 0 and j == 1:
                                    possible_coords.append((p_x, p_y, "down"))

            if not possible_coords:
                current_cell.draw()
                return
            else:
                next_x, next_y, direction = random.choice(possible_coords)
                next_cell = self._cells[next_x][next_y]

                if direction == "left":
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                elif direction == "right":
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                elif direction == "up":
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                elif direction == "down":
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False

                current_cell.draw()
                next_cell.draw()

                self._break_walls_r(next_x, next_y)