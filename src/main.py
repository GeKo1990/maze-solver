from window import Window
from cell import Cell

if __name__ == "__main__":
    window = Window(800, 600)

    # Create a list to hold the cells
    cells = []

    # Create cells with a size of 50 pixels
    cell_size = 50
    for i in range(5):
        for j in range(5):
            x1 = i * cell_size
            y1 = j * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            cell = Cell(x1, y1, x2, y2, window)
            cells.append(cell)

    # Draw all the cells
    for cell in cells:
        cell.draw()

    window.wait_for_close()
