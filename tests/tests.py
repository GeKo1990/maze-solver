import unittest
import sys
import os
import random

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from maze import Maze # type: ignore

class Tests(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.cell_size_x = 10
        self.cell_size_y = 10
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, None, 0)

    def test_maze_create_cells(self):
        self.assertEqual(len(self.maze._cells[0]), self.num_rows)
        self.assertEqual(len(self.maze._cells), self.num_cols)

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

    def test_no_window_provided(self):
        self.assertIsNone(self.maze._win)

    def test_break_entrance_and_exit(self):
        self.maze._break_entrance_and_exit()
        
        self.assertEqual(
            self.maze._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            self.maze._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall,
            False,
        )
    
    def test_reset_cells_visited(self):
        self.maze._reset_cells_visited()

        for x in range(self.num_cols):
            for y in range(self.num_rows):
                cell = self.maze._cells[x][y]
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
