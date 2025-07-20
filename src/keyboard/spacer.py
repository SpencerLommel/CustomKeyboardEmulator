# Spencer Lommel
# July 17th, 2025
# CustomKeyboardEmulator spacer.py

class Spacer:
    def __init__(self, width: float = 0, height: float = 0):
        self.width: float = width
        self.height: float = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __str__(self):
        return f'Spacer w:{self.width},h:{self.height}'

    def __eq__(self, other):
        return isinstance(other, Spacer) and self.width == other.width and self.height == other.height
