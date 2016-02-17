from ttt_board import TicTacToeBoard


class BasicTicTacToe:
    def __init__(self):
        self._board = TicTacToeBoard()
        self._board._current_player_turn = "X"
        return

    def play(self):
        while self._board.check_win_condition() is None or self._board.check_win_condition() != "draw":
            print('Please make your move:' + "/n")
            self._board.draw();
            location = int(raw_input('Choose a number(1-9): '))
            self._board.move(location)
            self._board.draw();
        if self._board.check_win_condition() != "draw":
            print("Player " + self._board.check_win_condition() + " wins!")
        else:
            print("Game draw!")

BasicTicTacToe().play()