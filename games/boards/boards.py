import numpy as np

class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size,size), dtype=int)

    def set_value(self, x, y, value):
        self.board[y, x] = value

    def print_board(self, valueDict):
        for row in self.board:
            for cellValue in row:
                print(valueDict.get(cellValue), end = " | ")
                print("\n")
