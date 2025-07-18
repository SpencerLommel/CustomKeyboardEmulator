# Spencer Lommel
# July 17th, 2025
# CustomKeyboardEmulator keyboard.py

from typing import Union
from .key import Key
from .spacer import Spacer

class Keyboard:
    def __init__(self):
        # contains an array of arrays, the outer one represents each column, and the inner ones represent each row
        self.rows: list[list[Union[Key, Spacer]]] = [[]]

    def add_row(self, row: list[Union[Key, Spacer]]):
        self.rows.append(row)

    def get_key(self, row: int, col: int) -> Union[Key, Spacer]:
        return self.rows[row][col]


    def __str__(self):
        return f'Keyboard: Not implemented yet so here is a silly face >:---)'
