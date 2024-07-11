import time
import random

from window import Window
from cell import Cell

class Maze:
    def __init__(
            self, x1, y1, num_rows: int, num_cols: int,
            cell_size_x: int, cell_size_y: int, win: Window = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._end_cell = None

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _reset_cells_visited(self):
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                cell = self._cells[x][y]
                cell.visited = False


    def _create_cells(self):
        for col_idx in range(self._num_cols):
            column = []
            for row_idx in range(self._num_rows):
                x1 = self._x1 + (col_idx * self._cell_size_x)
                x2 = self._x1 + ((col_idx + 1) * self._cell_size_x)
                y1 = self._y1 + (row_idx * self._cell_size_y)
                y2 = self._y1 + ((row_idx + 1) * self._cell_size_y)
                cell = Cell(x1, x2, y1, y2, self._win)
                column.append(cell)
                self._draw_cell(cell)
            self._cells.append(column)

    def _draw_cell(self, cell: Cell):
        if cell:
            cell.draw()
            self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        end = self._cells[self._num_cols - 1][self._num_rows - 1]

        start.has_top_wall = False
        end.has_bottom_wall = False
        self._end_cell = end
        self._draw_cell(start)
        self._draw_cell(end)

    def _break_walls_r(self, x, y):
        current_cell = self._cells[x][y]
        current_cell.visited = True

        while True:
            possible_coords = []

            if x > 0 and not self._cells[x - 1][y].visited:
                possible_coords.append((x - 1, y, "left"))

            if x < self._num_cols - 1 and not self._cells[x + 1][y].visited:
                possible_coords.append((x + 1, y, "right"))

            if y > 0 and not self._cells[x][y - 1].visited:
                possible_coords.append((x, y - 1, "up"))

            if y < self._num_rows - 1 and not self._cells[x][y + 1].visited:
                possible_coords.append((x, y + 1, "down"))

            if len(possible_coords) < 1:
                self._draw_cell(current_cell)
                return
            
            next_x, next_y, direction = random.choice(possible_coords)
            next_cell = self._cells[next_x][next_y]

            if direction == "left":
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
                
            if direction == "right":
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
                
            if direction == "up":
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                
            if direction == "down":
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False

            self._break_walls_r(next_x, next_y)

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, x, y):
        self._animate()

        current_cell = self._cells[x][y]
        current_cell.visited = True

        if current_cell == self._end_cell:
            return True
        
        directions = [(0, -1, "top"), (1, 0, "right"), (0, 1, "bottom"), (-1, 0, "left")]

        for i, j, direction in directions:
            pos_x = x + i
            pos_y = y + j
            has_possible_cell = pos_x >= 0 and pos_x <= self._num_cols - 1 and pos_y >= 0 and pos_y <= self._num_rows
            has_wall = getattr(current_cell, f"has_{direction}_wall")
            
            if has_possible_cell and not has_wall:
                possible_cell = self._cells[pos_x][pos_y]
                if not possible_cell.visited:
                    current_cell.draw_move(possible_cell)
                    if self._solve_r(pos_x, pos_y) == True:
                        return True
                    else:
                        current_cell.draw_move(possible_cell, True)
        
        return False


                

            

