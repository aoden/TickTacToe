class TicTacToeBoard:
    _width = 3
    _height = 3
    _coords = [[0 for x in range(_width)] for x in range(_height)]
    _num_to_coord = {1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (0, 1), 5: (1, 1), 6: (1, 2), 7: (0, 2), 8: (2, 1), 9: (2, 2)}
    _current_player_turn = "X"
    _number_allowed_to_win = 3
    _occupations = 0
    _win_paths = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7)]

    def __init__(self):
        for x in range(0, 3):
            for y in range(0, 3):
                self._coords[x][y] = TTTCell()
        return

    def draw(self):
        print(' ' + self._coords[0][0].value + ' | ' + self._coords[1][0].value + ' | ' + self._coords[2][0].value)
        print('--------')
        print(' ' + self._coords[0][1].value + ' | ' + self._coords[1][1].value + ' | ' + self._coords[1][2].value)
        print('--------')
        print(' ' + self._coords[0][2].value + ' | ' + self._coords[2][1].value + ' | ' + self._coords[2][2].value)

    def move(self, location):
        x, y = self._num_to_coord[location]
        if self.check_valid_move(location):
            self._occupations += 1
            self._coords[x][y].player = self._current_player_turn
            self._coords[x][y].value = self._current_player_turn
        else:
            print("This is not a valid move!")
        if self._current_player_turn == "X":
            self._current_player_turn = "O"
        else:
            self._current_player_turn = "X"

    def print_cell(self, cell):
        print cell.value

    def check_valid_move(self, location):
        x, y = self._num_to_coord[location]
        if 9 >= location >= 1 and self._coords[x][y].player is None:
            return True
        return False

    def get_cell(self, location):
        if 9 >= location >= 1:
            x, y = self._num_to_coord[location]
            return self._coords[x][y]
        return None

    def check_win_condition(self):
        if self._occupations == self._width * self._height:
            return "draw"
        for path in self._win_paths:
            a, b, c = path
            if self.get_cell(a).player == self.get_cell(b).player == self.get_cell(c).player:
                return self.get_cell(a).player
        return None


class TTTCell:
    def __init__(self):
        self.player = None
        self.value = ""
