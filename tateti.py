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
        lugar = self.board
        if lugar[0] == ' ':
            return pos
        elif lugar[1] == ' ':
            return pos
        elif lugar[2] == ' ':
            return pos
        elif lugar[3] == ' ':
            return pos
        elif lugar[4] == ' ':
            return pos
        elif lugar[5] == ' ':
            return pos
        elif lugar[6] == ' ':
            return pos
        elif lugar[7] == ' ':
            return pos
        elif lugar[8] == ' ':
            return pos
        else:
            return False
    
    def assign(self, pos, piece):
        validate = self.validate(pos)
        if validate == pos:
            for v in self.board[pos]:
                self.board.remove(v)
                self.board.append(piece)
                return self.board
        else:
            raise Exception
