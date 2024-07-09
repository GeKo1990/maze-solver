import unittest
import sys
import os
import random

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from maze import Maze # type: ignore
from cell import Cell # type: ignore

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

    def test_break_entrance_and_exit(self):
        random.seed(0)  # Setting the seed for reproducibility
        self.maze._break_entrance_and_exit()
        start = self.maze._cells[0][0]
        end = self.maze._cells[self.num_rows - 1][self.num_cols - 1]
        
        # Check that one of the walls is broken at the start cell
        self.assertTrue(
            not start.has_right_wall or not start.has_bottom_wall
        )
        
        # Check that one of the walls is broken at the end cell
        self.assertTrue(
            not end.has_left_wall or not end.has_top_wall
        )
        

if __name__ == "__main__":
    unittest.main()
