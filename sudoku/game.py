import numpy as np


def is_valid(position, number):
    pos_x = position[0]
    pos_y = position[1]

    row = board[pos_x]
    col = board[:, pos_y]
    if number in row or number in col:
        return False
    x_3x3 = pos_x // 3 * 3
    y_3x3 = pos_y // 3 * 3
    block_3x3 = board[x_3x3:x_3x3 + 3, y_3x3:y_3x3 + 3]
    if number in block_3x3:
        return False
    return True


def get_next_position(board, position):
    next_x = position[0]
    next_y = position[1]
    while board[next_x][next_y] != 0:
        next_y += 1
        if next_y >= len(board):
            next_y = 0
            next_x += 1
        if next_x not in range(len(board)) or next_y not in range(len(board)):
            return [-1, -1]
    return [next_x, next_y]


def back(board, position=None):
    if position is None:
        position = [0, 0]
    if position == [-1, -1]:
        print("successful")
        print(board)
        return True
    pos_x = position[0]
    pos_y = position[1]
    pos_value = board[pos_x][pos_y]
    if pos_value == 0:
        for number in range(1, 10):
            if is_valid(position, number):
                board[pos_x][pos_y] = number
                next_position = get_next_position(board, position)
                if back(board, next_position) is True:
                    return True
                else:
                    board[pos_x][pos_y] = 0
    else:
        next_position = get_next_position(board, position)
        back(board, next_position)
    return False


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
board = np.array(board)
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == '.':
            board[i][j] = 0
        else:
            board[i][j] = int(board[i][j])
board = board.astype('int32')

# board = np.zeros((9, 9))
print(board)
back(board)

