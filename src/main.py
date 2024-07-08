from window import Window
from maze import Maze

if __name__ == "__main__":
    window = Window(800, 600)

    maze = Maze(0, 0, 10, 12, 50, 50, window)
    print(f"cells: {len(maze._cells)}")

    window.wait_for_close()
