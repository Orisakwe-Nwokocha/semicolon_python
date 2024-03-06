from typing import List

from tictactoe.cell_type import CellType
from tictactoe.invalid_position_error import InvalidPositionError
from tictactoe.player import Player


class TicTacToe:
    def __init__(self, player_one_id: int, player_two_id: int):
        self.__position_board = [[CellType.EMPTY, CellType.EMPTY, CellType.EMPTY],
                                 [CellType.EMPTY, CellType.EMPTY, CellType.EMPTY],
                                 [CellType.EMPTY, CellType.EMPTY, CellType.EMPTY]]

        player_one_cell_type: CellType = CellType.X if player_one_id == 1 else CellType.O
        player_two_cell_type: CellType = CellType.O if player_two_id == 2 else CellType.X

        self.__playerOne: Player = Player(player_one_id, player_one_cell_type)
        self.__playerTwo: Player = Player(player_two_id, player_two_cell_type)

        self.__winner = None

    def get_position_board(self) -> List[List[CellType]]:
        return self.__position_board

    def mark_position(self, player_id: int, square: int):
        TicTacToe.__validate_range(square)

        row = (square // 3) - 1 if square % 3 == 0 else square // 3
        column = 2 if square % 3 == 0 else (square % 3) - 1

        self.__validate(row, column)

        player = self.__get_player(player_id)
        self.__position_board[row][column] = player.get_cell_type()

        if self.__is_winner():
            self.__winner = player

    def __is_winner(self) -> bool:
        for index in range(3):
            if self.__is_horizontal(index):
                return True
            elif self.__is_vertical(index):
                return True
        if self.__is_left_diagonal():
            return True
        else:
            return self.__is_right_diagonal()

    def __is_right_diagonal(self) -> bool:
        return self.__is_winner_helper(0, -2, 1, -1)

    def __is_left_diagonal(self) -> bool:
        return self.__is_winner_helper(0, 0, 1, 1)

    def __is_vertical(self, index: int) -> bool:
        return self.__is_winner_helper(0, index, 1, 0)

    def __is_horizontal(self, index: int) -> bool:
        return self.__is_winner_helper(index, 0, 0, 1)

    def __is_winner_helper(self, start_row: int, start_column: int, row_increment: int, column_increment: int) -> bool:
        number_of_x = 0
        number_of_o = 0

        for index in range(3):
            row = (start_row + index) * row_increment
            column = (start_column + index) * column_increment

            cell_type: CellType = self.__position_board[row][column]

            if cell_type == CellType.X:
                number_of_x += 1
            elif cell_type == CellType.O:
                number_of_o += 1

        if number_of_x == 3:
            return True
        else:
            return number_of_o == 3

    def get_winner(self) -> Player:
        return self.__winner

    def display_board(self) -> str:
        horizontal = "=" * 13
        vertical = "|"
        blank = " "

        board = ""

        for row in range(3):
            board += horizontal + "\n"

            board = self.__display_board_helper(row, blank, board, vertical)
            board += vertical + "\n"

            if row == 2:
                return board + horizontal

    def __display_board_helper(self, row: int, blank: str, board: str, vertical: str) -> str:
        for column in range(3):
            cell_type = self.__position_board[row][column]
            position = blank if cell_type == CellType.EMPTY else cell_type

            board += vertical + blank + str(position) + blank

        return board

    def is_board_full(self) -> bool:
        for cell_types in self.__position_board:
            for cell_type in cell_types:
                if cell_type == CellType.EMPTY:
                    return False

        return True

    @staticmethod
    def __validate_range(square: int):
        is_out_of_range = square < 1 or square > 9

        if is_out_of_range:
            raise ValueError("Square must be between 1 and 9")

    def __validate(self, row: int, column: int):
        is_filled = self.__position_board[row][column] != CellType.EMPTY

        if is_filled:
            raise InvalidPositionError("Position is already taken.")

    def __get_player(self, player_id: int) -> Player:
        if self.__playerOne.get_id() == player_id:
            return self.__playerOne

        return self.__playerTwo

    def get_players(self) -> List[Player]:
        players = [self.__playerOne, self.__playerTwo]

        return players
