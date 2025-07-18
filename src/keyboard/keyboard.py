# Spencer Lommel
# July 17th, 2025
# CustomKeyboardEmulator keyboard.py

from typing import Union

from .key import Key
from .spacer import Spacer


def calculate_size(matrix):
    count = 0
    for row in matrix:
        count += len(row)
    return count


class Keyboard:
    def __init__(self, rows: list[list[Union[Key, Spacer]]] = []):
        # contains an array of arrays, the outer one represents each column, and the inner ones represent each row
        self.rows: list[list[Union[Key, Spacer]]] = rows
        self.height = len(rows)
        # not sure how we should implement width because not all rows will have the same number of keys hmmm
        # for now we just set width to keys in the first column, but probably not ideal
        self.width = 0
        self.size = self.__calculate_size(rows)

    def add_row(self, row: list[Union[Key, Spacer]]):
        self.rows.append(row)
        self.__update_sizing()

    def get_key(self, row: int, col: int) -> Union[Key, Spacer]:
        return self.rows[row][col]

    def remove_row(self, row: int):
        self.rows.pop(row)
        self.__update_sizing()

    def __str__(self):
        return f'Keyboard: Not implemented yet so here is a silly face >:---)'

    @staticmethod
    def __calculate_size(matrix):
        count = 0
        for row in matrix:
            count += len(row)
        return count

    def __update_sizing(self):
        self.size = self.__calculate_size(self.rows)
        self.height = len(self.rows)
        self.width = len(self.rows[0])

    def __eq__(self, other):
        # Because we are checking the row data, we shouldn't need to check height/width/size
        self.rows == other.rows and isinstance(other, Keyboard)
