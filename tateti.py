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

    def validate(self, position):
        if self.board[position-1] == ' ':
            return True
        return False

    def assign(self, position, piece):
        boolean = self.validate(position)
        if boolean is True:
            self.board[position-1] = piece
        else:
            raise Exception
    
    def draw_board(self):
        lista = [" " for _ in range(9)]
        for i in range(9):
            if self.board[i] == " ":
                lista[i] = i+1
                continue
            lista[i] = self.board[i]
        display = (f'\n {lista[0]} | {lista[1]} | {lista[2]}'
                   f' \n---+---+---\n {lista[3]} | {lista[4]}'
                   f' | {lista[5]} \n---+---+---\n {lista[6]}'
                   f' | {lista[7]} | {lista[8]} \n')
        return display