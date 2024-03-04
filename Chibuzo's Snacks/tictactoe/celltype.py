from enum import Enum


class CellType(Enum):
    O = 'O'
    X = 'X'
    EMPTY = 'EMPTY'

    def __repr__(self):
        return str(self.value)



