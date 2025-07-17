class Spacer:
    def __init__(self, width: float = 0, height: float = 0):
        self.width: float = width
        self.height: float = height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def __str__(self):
        return f'Spacer w:{self.width},h:{self.height}'