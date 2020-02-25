import unittest
import numpy as np
from game import *

board = np.zeros((9, 9))
for i in range(9):
    board[0][i] = i + 1
    x, y = BLOCK[i]
    board[x][y] = i + 1
    board[i][8] = 9 - i
board = board.astype('int32')

# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# board = np.array(board)
# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if board[i][j] == '.':
#             board[i][j] = 0
#         else:
#             board[i][j] = int(board[i][j])
# board = board.astype('int32')


class TestMethods(unittest.TestCase):

    def test_1(self):
        assert nth_block_valid(board, 0)

    def test_2(self):
        assert n_th_row_valid(board, 0)

    def test_3(self):
        assert n_th_col_valid(board, 8)


if __name__ == '__main__':
    unittest.main()
