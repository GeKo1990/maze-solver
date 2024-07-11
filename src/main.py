from window import Window
from maze import Maze

if __name__ == "__main__":
    window = Window(800, 600)

    maze = Maze(50, 50, 10, 14, 50, 50, window)

    window.wait_for_close()
