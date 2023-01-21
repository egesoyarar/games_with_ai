import random
import numpy as np

from games.boards.boards import Board


class TicTacToeBoard(Board):
    def __init__(self, size):
        super().__init__(size)

    def is_full(self):
        return np.all(self.board != 0)

    def check_status(self):
        return self.horitontal_check() or self.vertical_check() or self.cross_check()

    def is_available(self, x, y):
        return self.board[y, x] == 0

    def horitontal_check(self):
        for row in self.board:
            hTotal = sum(row)
            if hTotal == self.size:
                return 1
            elif hTotal == -self.size:
                return -1
        return 0

    def vertical_check(self):
        for col in self.board.T:
            vTotal = sum(col)
            if vTotal == self.size:
                return 1
            elif vTotal == -self.size:
                return -1
        return 0

    def cross_check(self):
        if sum(np.diagonal(self.board)) == self.size or sum(
                np.diagonal(np.fliplr(self.board))) == self.size:
            return 1
        elif sum(np.diagonal(self.board)) == -self.size or sum(
                np.diagonal(np.fliplr(self.board))) == -self.size:
            return -1
        return 0
