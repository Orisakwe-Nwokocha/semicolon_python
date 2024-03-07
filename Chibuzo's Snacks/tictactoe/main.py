import random
from tkinter import messagebox, simpledialog

from tictactoe.invalid_position_error import InvalidPositionError
from tictactoe.player import Player
from tictactoe.tic_tac_toe import TicTacToe


class Main:
    @classmethod
    def start_app(cls):
        cls.__print_message("Game loading...", "Welcome, players")

        cls.__select_type()

    @classmethod
    def __select_type(cls):
        user_choice = cls.get_choice("Player 1, do you want to use X?")

        if user_choice:
            game: TicTacToe = TicTacToe(1, 2)
        else:
            game: TicTacToe = TicTacToe(2, 1)

        player_one: Player = game.get_players()[0]
        player_two: Player = game.get_players()[1]

        cls.__print_message("Info", "Player 1 is " + str(player_one.get_cell_type()))
        cls.__print_message("Info", "Player 2 is " + str(player_two.get_cell_type()))

        cls.__play_game(game)

    @classmethod
    def __play_game(cls, game: TicTacToe):
        choice = Main.get_choice("Do you want to play against computer?")
        cls.__print_message("Display board", game.display_board())

        player_one = game.get_players()[0]

        if choice:
            cls.__play_vs_computer(game, player_one)

        # playVsHuman(playerOne);

    @classmethod
    def __play_vs_computer(cls, game: TicTacToe, player_one: Player):
        computer = game.get_players()[1]

        cls.__player_one_move(game, player_one)

        cls.__computer_move(game, computer)

        is_full = game.is_board_full()
        if not is_full:
            cls.__play_vs_computer(game, player_one)

    @classmethod
    def __player_one_move(cls, game: TicTacToe, player_one: Player):
        is_invalid = True

        while is_invalid:
            try:
                player_one_position = cls.__user_input("Make your move", "Player 1, select a position (1-9)")
                player_one.play(game, int(player_one_position))
                cls.__print_message("Display board", game.display_board())

                cls.__check_game_status()
                is_invalid = False
            except Exception as e:
                messagebox.showerror("Error", str(e))

    @classmethod
    def __computer_move(cls, game: TicTacToe, computer: Player):
        is_invalid = True

        while is_invalid:
            computer_move = random.randint(1, 10)
            print(computer_move)
            try:
                computer.play(game, computer_move)
                cls.__print_message("Display board", game.display_board())

                cls.__check_game_status()
                is_invalid = False
            except (ValueError, InvalidPositionError):
                pass

    # isInvalidMove = true;
    # while (isInvalidMove) {
    # int computerMove = random.nextInt(1, 10);
    # try {
    # computer.play(game, computerMove);
    # print(game.displayBoard(), "Display board");
    #
    # checkGameStatus();
    # isInvalidMove = false;
    # }
    # catch(RuntimeException
    # ignored) {}

    # private
    # static
    # void
    # playVsHuman(Player
    # playerOne) {
    #     Player
    # playerTwo = game.getPlayers()[1];
    #
    # playerOneMove(playerOne);
    # playerTwoMove(playerTwo);
    #
    # boolean
    # gameIsOn = !game.isBoardFull();
    # if (gameIsOn)
    # playVsHuman(playerOne);
    # }
    #
    # private
    # static
    # void
    # playerTwoMove(Player
    # playerTwo) {
    #     isInvalidMove = true;
    # while (isInvalidMove) {
    # try {
    # String playerTwoPosition = input("Player 2, select a position (1-9)");
    # playerTwo.play(game, Integer.parseInt(playerTwoPosition));
    # print(game.displayBoard(), "Display board");
    #
    # checkGameStatus();
    # isInvalidMove = false;
    # }
    # catch(RuntimeException
    # e) {
    #     displayErrorMessage(e);
    # }
    # }
    # }
    #

    @classmethod
    def __check_game_status(cls):
        pass

    #     boolean
    # isWinnerNull = game.getWinner() == null;
    #
    # if (!isWinnerNull)
    # declareWinner();
    # if (game.isBoardFull())
    # declareDraw();
    # }

    # private
    # static
    # void
    # declareDraw()
    # {
    #     print("Game ended in a draw", "Status");
    # print(game.displayBoard(), "Display board");
    # exit();
    # }
    #
    # private
    # static
    # void
    # exit()
    # {
    #     print("Thank you for playing our game!!!", "Goodbye");
    # System.exit(0);
    # }
    #
    # private
    # static
    # void
    # declareWinner()
    # {
    #     print(game.getWinner().toString() + " is the winner!!!", "Champion");
    # print(game.displayBoard(), "Display board");
    # exit();
    # }

    @classmethod
    def __print_message(cls, title: str, message: str):
        messagebox.showinfo(title, message)

    @classmethod
    def __user_input(cls, title: str, prompt: str, ) -> str:
        return simpledialog.askstring(title, prompt)

    @classmethod
    def get_choice(cls, message) -> bool:
        return messagebox.askyesno("Select option", message)


if __name__ == "__main__":
    Main.start_app()
