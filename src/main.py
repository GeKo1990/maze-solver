from window import Window
from maze import Maze

if __name__ == "__main__":
    window = Window(800, 600)

    maze = Maze(55, 40, 30, 30, 23, 18, window)
    maze.solve()

    window.wait_for_close()
