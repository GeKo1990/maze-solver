from window import Window
from line import Line
from point import Point

if __name__ == "__main__":
    window = Window(800, 600)

    # testing draw line
    window.draw_line(Line(Point(0,0), Point(15,20)), "black")
    window.draw_line(Line(Point(30,30), Point(15,20)), "red")

    window.wait_for_close()
