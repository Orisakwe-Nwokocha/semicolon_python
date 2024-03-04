from tictactoe.celltype import CellType


class Player:
    def __init__(self, player_id: int, cell_type: CellType):
        self.__player_id = player_id
        self.__cell_type = cell_type

    def get_cell_type(self):
        return self.__cell_type

    def get_id(self):
        return self.__player_id
