class TaTeTi:
    def __init__(self, board=[' ' for _ in range(9)]):
        self.board = board
    
    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    def full(self):
        for v in self.board:
            if v == ' ':
                return False
        return self.board

    def win(self):
        board = self.board
        row = board[0] == board[1] == board[2]
        if row and self.board[0] == 'x' or row and self.board[0] == 'o':
            return True
        row = board[3] == board[4] == board[5]
        if row and self.board[3] == 'x' or row and self.board[3] == 'o':
            return True
        row = board[6] == board[7] == board[8]
        if row and self.board[6] == 'x' or row and self.board[6] == 'o':
            return True
        row = board[0] == board[3] == board[6]
        if row and self.board[0] == 'x' or row and self.board[0] == 'o':
            return True
        row = board[1] == board[4] == board[7]
        if row and self.board[1] == 'x' or row and self.board[1] == 'o':
            return True
        row = board[2] == board[5] == board[8]
        if row and self.board[2] == 'x' or row and self.board[2] == 'o':
            return True
        row = board[0] == board[4] == board[8]
        if row and self.board[0] == 'x' or row and self.board[0] == 'o':
            return True
        row = board[2] == board[4] == board[6]
        if row and self.board[2] == 'x' or row and self.board[2] == 'o':
            return True
        return False

    def validate(self, pos):
        num = pos - 1
        for _ in range(0, 9):
            if self.board[num] == ' ':
                return True
        return False

    def assign(self, pos, piece):
        validate = self.validate(pos)
        if validate is True:
            self.board[pos - 1] = piece
            return self.board
        else:
            raise Exception

    def draw_board(self):
        w = ('---+---+---')
        if self.board[0] and self.board[1] and self.board[2] != ' ':
            x = ' {a} | {b} | {c} '.format(a=self.board[0], b=self.board[1],
                                           c=self.board[2])
        if self.board[0] and self.board[1] and self.board[2] != ' ':
            y = ' {a} | {b} | {c} '.format(a=self.board[3], b=self.board[4],
                                           c=self.board[5])
        if self.board[0] and self.board[1] and self.board[2] != ' ':
            z = ' {a} | {b} | {c} '.format(a=self.board[6], b=self.board[7],
                                           c=self.board[8])
        if self.board[0] or self.board[1] or self.board[2] == ' ':
            x = ' 1 | 2 | 3 '
        if self.board[0] or self.board[1] or self.board[2] == ' ':
            y = ' 4 | 5 | 6 '
        if self.board[0] or self.board[1] or self.board[2] == ' ':
            z = ' 7 | 8 | 9 '
        return ("\n".join((x, w, y, w, z)))