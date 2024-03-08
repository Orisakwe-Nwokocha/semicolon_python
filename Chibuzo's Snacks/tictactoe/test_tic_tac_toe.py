import unittest

from tictactoe.cell_type import CellType
from tictactoe.invalid_position_error import InvalidPositionError
from tictactoe.player import Player
from tictactoe.tic_tac_toe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe_game = TicTacToe(1, 2)
        self.empty = CellType.EMPTY
        self.testPositionBoard = [[self.empty] * 3] * 3

    def test_that_there_are_two_players_in_game(self):
        players = self.tic_tac_toe_game.get_players()
        number_of_players = len(players)

        self.assertEqual(2, number_of_players)

    def test_that_players_have_unique_id(self):
        players = self.tic_tac_toe_game.get_players()
        player_one: Player = players[0]
        player_two: Player = players[1]

        self.assertEqual(1, player_one.get_id())
        self.assertEqual(2, player_two.get_id())

    def test_that_game_has_position_board(self):
        position_board = self.tic_tac_toe_game.get_position_board()

        self.assertListEqual(self.testPositionBoard, position_board)

    def test_that_board_is_filled_with_dummy_enum_values_by_default(self):
        position_board = self.tic_tac_toe_game.get_position_board()

        self.assertListEqual(self.testPositionBoard, position_board)

    def test_that_player_one_has_enum_value_X(self):
        players = self.tic_tac_toe_game.get_players()
        player_one = players[0]

        self.assertEqual(CellType.X, player_one.get_cell_type())

    def test_that_player_two_has_enum_value_O(self):
        players = self.tic_tac_toe_game.get_players()
        player_two = players[1]

        self.assertEqual(CellType.O, player_two.get_cell_type())

    def test_that_players_can_choose_any_enum_constant_playerOneHasEnumValueO_playerTwoHasEnumValueX(self):
        tic_tac_toe_game = TicTacToe(2, 1)
        players = tic_tac_toe_game.get_players()
        player_one = players[0]
        player_two = players[1]

        self.assertEqual(CellType.O, player_one.get_cell_type())
        self.assertEqual(CellType.X, player_two.get_cell_type())

    def test_that_game_can_mark_position(self):
        position_board = self.tic_tac_toe_game.get_position_board()
        self.tic_tac_toe_game.mark_position(1, 1)
        self.assertNotEqual(CellType.EMPTY, position_board[0][0])
        self.assertEqual(CellType.X, position_board[0][0])

        self.tic_tac_toe_game.mark_position(2, 5)
        self.assertNotEqual(CellType.EMPTY, position_board[1][1])
        self.assertEqual(CellType.O, position_board[1][1])

        self.tic_tac_toe_game.mark_position(1, 9)
        self.assertNotEqual(CellType.EMPTY, position_board[2][2])
        self.assertEqual(CellType.X, position_board[2][2])

    def test_player_marks_position_out_of_range_valueError_is_raised(self):
        self.assertRaises(ValueError, self.tic_tac_toe_game.mark_position, 1, 0)
        self.assertRaises(ValueError, self.tic_tac_toe_game.mark_position, 1, 10)

    def test_player_marks_non_empty_position_invalidPositionError_is_raised(self):
        self.tic_tac_toe_game.mark_position(1, 1)
        self.assertRaises(InvalidPositionError, self.tic_tac_toe_game.mark_position, 1, 1)

    def test_player_marks_non_empty_position_invalidPositionException_is_thrown_test_error_message(self):
        self.tic_tac_toe_game.mark_position(1, 1)

        try:
            self.tic_tac_toe_game.mark_position(1, 1)
        except InvalidPositionError as e:
            self.assertEqual("Position is already taken.", str(e))

    def test_that_players_can_play_game(self):
        game = TicTacToe(2, 1)
        players = game.get_players()
        player_one = players[0]
        player_two = players[1]

        for count in range(1, 10, 2):
            player_one.play(game, count)
            if count == 9:
                break
            player_two.play(game, count + 1)

        position_board = game.get_position_board()

        self.assertNotEqual(CellType.EMPTY, position_board[0][0])
        self.assertNotEqual(CellType.EMPTY, position_board[1][1])
        self.assertNotEqual(CellType.EMPTY, position_board[2][2])

    def test_that_game_can_determine_winner_horizontally(self):
        self.tic_tac_toe_game.mark_position(1, 1)
        self.tic_tac_toe_game.mark_position(1, 2)
        self.tic_tac_toe_game.mark_position(1,  3)

        self.assertIsNotNone(self.tic_tac_toe_game.get_winner())
        self.assertEqual(CellType.X, self.tic_tac_toe_game.get_winner().get_cell_type())

    def test_that_game_can_determine_winner_vertically(self):
        self.tic_tac_toe_game.mark_position(2, 3)
        self.tic_tac_toe_game.mark_position(2, 6)
        self.tic_tac_toe_game.mark_position(2, 9)

        self.assertIsNotNone(self.tic_tac_toe_game.get_winner())
        self.assertEqual(CellType.O, self.tic_tac_toe_game.get_winner().get_cell_type())

    def test_that_game_can_determine_winner_left_diagonal(self):
        self.tic_tac_toe_game.mark_position(1, 1)
        self.tic_tac_toe_game.mark_position(1, 5)
        self.tic_tac_toe_game.mark_position(1, 9)

        self.assertIsNotNone(self.tic_tac_toe_game.get_winner())
        self.assertEqual(CellType.X, self.tic_tac_toe_game.get_winner().get_cell_type())

    def test_that_game_can_determine_winner_right_diagonal(self):
        self.tic_tac_toe_game.mark_position(2, 3)
        print(self.tic_tac_toe_game.get_winner())
        self.tic_tac_toe_game.mark_position(2, 5)
        self.tic_tac_toe_game.mark_position(2, 7)

        self.assertIsNotNone(self.tic_tac_toe_game.get_winner())
        self.assertEqual(CellType.O, self.tic_tac_toe_game.get_winner().get_cell_type())

    def test_display_board(self):
        players = self.tic_tac_toe_game.get_players()
        player_one = players[0]
        player_two = players[1]

        for count in range(1, 10, 2):
            player_one.play(self.tic_tac_toe_game, count)
            print(self.tic_tac_toe_game.display_board())

            if count == 9:
                break
            player_two.play(self.tic_tac_toe_game, count + 1)

            if not self.tic_tac_toe_game.is_board_full():
                print(self.tic_tac_toe_game.display_board())

        if self.tic_tac_toe_game.is_board_full():
            print(self.tic_tac_toe_game.display_board())
        print(self.tic_tac_toe_game.get_winner())

