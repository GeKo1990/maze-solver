import time

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

        #self._animate()

    def _animate(self):
        while(self._win):
            self._win.redraw()
            time.sleep(0.05)