class Point:
    def __init__(self, x: int | tuple, y: int | None = None):
        if isinstance(x, tuple):
            self.x, self.y = x
        else:
            self.x = x
            self.y = y