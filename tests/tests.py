import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from maze import Maze # type: ignore
from cell import Cell # type: ignore

class MockWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_line(self, line, color):
        pass

    def redraw(self):
        pass

class Tests(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.cell_size_x = 10
        self.cell_size_y = 10
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y)

    def test_maze_create_cells(self):
        self.assertEqual(len(self.maze._cells), self.num_rows)
        self.assertEqual(len(self.maze._cells[0]), self.num_cols)

    def test_cell_coordinates(self):
        cell = self.maze._cells[0][0]
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._x2, 10)
        self.assertEqual(cell._y1, 0)
        self.assertEqual(cell._y2, 10)

    def test_cell_coordinates_middle(self):
        cell = self.maze._cells[5][5]
        self.assertEqual(cell._x1, 50)
        self.assertEqual(cell._x2, 60)
        self.assertEqual(cell._y1, 50)
        self.assertEqual(cell._y2, 60)

    def test_cell_coordinates_last(self):
        cell = self.maze._cells[self.num_rows - 1][self.num_cols - 1]
        self.assertEqual(cell._x1, (self.num_cols - 1) * self.cell_size_x)
        self.assertEqual(cell._x2, self.num_cols * self.cell_size_x)
        self.assertEqual(cell._y1, (self.num_rows - 1) * self.cell_size_y)
        self.assertEqual(cell._y2, self.num_rows * self.cell_size_y)

    def test_no_window_provided(self):
        self.assertIsNone(self.maze._win)

    def test_window_provided(self):
        window = MockWindow(100, 100)
        maze_with_win = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, window)
        self.assertEqual(maze_with_win._win, window)

if __name__ == "__main__":
    unittest.main()
