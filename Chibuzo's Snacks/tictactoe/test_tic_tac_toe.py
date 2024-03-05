import unittest

from tictactoe.cell_type import CellType
from tictactoe.player import Player
from tictactoe.tic_tac_toe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        self.ticTacToeGame = TicTacToe(1, 2)
        self.empty = CellType.EMPTY
        self.testPositionBoard = [[self.empty] * 3] * 3

    def test_that_there_are_two_players_in_game(self):
        players = self.ticTacToeGame.get_players()
        number_of_players = len(players)

        self.assertEqual(2, number_of_players)

    def test_that_players_have_unique_id(self):
        players = self.ticTacToeGame.get_players()
        player_one: Player = players[0]
        player_two: Player = players[1]

        self.assertEqual(1, player_one.get_id())
        self.assertEqual(2, player_two.get_id())

    def test_that_game_has_position_board(self):
        position_board = self.ticTacToeGame.get_position_board()

        self.assertListEqual(self.testPositionBoard, position_board)
