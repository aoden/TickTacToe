class TicTacToeBoard:
    _width = 3
    _height = 3
    _coords = [[0 for x in range(_width)] for x in range(_height)]
    _num_to_coord = {1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (0, 1), 5: (1, 1), 6: (1, 2), 7: (0, 2), 8: (2, 1), 9: (2, 2)}
    _current_player_turn = "X"
    _number_allowed_to_win = 3
    _occupations = 0

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
            return True;
        return False;

    def check_win_condition(self):
        if self._occupations == self._width * self._height:
            return "draw"
        for i in range(0, 3):
            if self._coords[0][i].player is not None and (
                            self._coords[0][i].value == self._coords[1][i].value == self._coords[2][i].value):
                return self._coords[0][i].player
            if self._coords[i][0].player is not None and (
                            self._coords[i][0].value == self._coords[i][1].value == self._coords[i][2].value):
                return self._coords[0][i].player
        if self._coords[0][0].player is not None and self._coords[0][0].value == self._coords[1][1].value == \
                self._coords[2][2].value:
            return self._coords[0][0].player
        if self._coords[2][0].player is not None and self._coords[2][1].value == self._coords[2][2].value == \
                self._coords[2][0].value:
            return self._coords[2][0].player
        return None


class TTTCell:
    def __init__(self):
        self.player = None
        self.value = ""
