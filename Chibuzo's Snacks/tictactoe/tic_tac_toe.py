from typing import List

from tictactoe.celltype import CellType
from tictactoe.invalid_position_error import InvalidPositionError
from tictactoe.player import Player


class TicTacToe:
    def __init__(self, player_one_id: int, player_two_id: int):
        self.__position_board = [[CellType.EMPTY] * 3] * 3

        player_one_cell_type: CellType = CellType.X if player_one_id == 1 else CellType.O
        player_two_cell_type: CellType = CellType.O if player_two_id == 2 else CellType.X

        self.__playerOne: Player = Player(player_one_id, player_one_cell_type)
        self.__playerTwo: Player = Player(player_two_id, player_two_cell_type)

    def get_player_one(self) -> Player:
        return self.__playerOne

    def get_player_two(self) -> Player:
        return self.__playerTwo

    def get_board(self) -> List[List[CellType]]:
        return self.__position_board

    def mark_position(self, player_id: int, square: int):
        TicTacToe.__validate_range(square)

        row = (square / 3) - 1 if square % 3 == 0 else square / 3
        column = (square / 3) - 1 if square % 3 == 0 else (square % 3) - 1
        if square % 3 == 0:
            column = 2

        self.__validate(int(row), int(column))

        player = self.__get_player(player_id)
        self.__position_board[int(row)][int(column)] = player.get_cell_type()

        # checkForWinner()

    @staticmethod
    def __validate_range(square: int):
        is_out_of_range = square < 1 or square > 9
        if is_out_of_range: raise ValueError("Square must be between 1 and 9")

    def __validate(self, row: int, column: int):
        is_filled = self.__position_board[row][column] != CellType.EMPTY
        if is_filled: raise InvalidPositionError("Position is already taken.")

    def __get_player(self, player_id: int) -> Player:
        if self.__playerOne.get_id() == player_id:
            return self.__playerOne
        return self.__playerTwo


if __name__ == "__main__":
    tic_tac_toe = TicTacToe(2, 1)
    print(tic_tac_toe.get_player_one().get_cell_type())
    print(tic_tac_toe.get_player_two().get_cell_type())
    print(tic_tac_toe.get_board())
