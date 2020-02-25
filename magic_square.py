import numpy as np
from itertools import permutations
import math
import time
from copy import deepcopy


def check(arr):
    horizontal = np.sum(arr, axis=1)
    vertical = np.sum(arr, axis=0)

    diagonal = [sum(arr[i][i] for i in range(len(arr))), sum(np.flip(arr.T, axis=1)[i][i] for i in range(len(arr)))]

    return (len(set(horizontal)) == 1) and (len(set(vertical)) == 1) and (len(set(diagonal)) == 1)


def ms(n):
    count = 0
    for i in permutations(range(1, n ** 2 + 1)):
        table = np.array(i).reshape((n, n))
        count += 1
        if check(table):
            print(f"searched for {count} in {math.factorial(n ** 2)} possbile solutions")
            print(table)
            break


def count_time(fn, n):
    a = time.time()
    fn(n)
    print(f"takes {time.time() - a:.2f} s")


# takes forever
# a = time.time()
# ms(4)
# print(f"takes {time.time() - a:.2f} s")


def backtrack(n):
    each_row = sum(range(1, n ** 2 + 1)) / n

    def back(board, position=[0, 0]):
        if position == [-1, -1]:
            print("success")
            print(board)
            return True

        pos_x = position[0]
        pos_y = position[1]
        pos_value = board[pos_x][pos_y]
        if pos_value == 0:
            for number in range(1, n ** 2 + 1):
                if is_valid(position, number, each_row):
                    board[pos_x][pos_y] = number
                    next_position = get_next_position(board, position)
                    if back(board, next_position) is True:
                        return True
                    else:
                        board[pos_x][pos_y] = 0
                else:
                    board[pos_x][pos_y] = 0
        else:
            next_position = get_next_position(board, position)
            back(board, next_position)
        return False

    back(board)
    return


def is_valid(position, number, each_row):
    if number in board:
        return False
    # cp_board = deepcopy(board)
    cp_board = board
    pos_x = position[0]
    pos_y = position[1]
    cp_board[pos_x][pos_y] = number
    col = cp_board[:, pos_y]
    row = cp_board[pos_x]
    diagonal_1 = cp_board.diagonal()
    diagonal_2 = np.fliplr(cp_board).diagonal()

    if 0 not in col and sum(col) != each_row:
        return False
    elif 0 not in row and sum(row) != each_row:
        return False
    elif 0 not in diagonal_1 and sum(diagonal_1) != each_row:
        return False
    elif 0 not in diagonal_2 and sum(diagonal_2) != each_row:
        return False
    return True


def get_next_position(board, position):
    pos_x = position[0]
    pos_y = position[1]
    while board[pos_x][pos_y] != 0:
        pos_y += 1
        if pos_y >= len(board):
            pos_x += 1
            pos_y = 0
        if pos_x not in range(len(board)) or pos_y not in range(len(board)):
            return [-1, -1]
    return [pos_x, pos_y]


board = np.zeros((4, 4))
board[0][0:4] = [2, 16, 13, 3]
# board[1][0:4] = [11, 5, 8, 10]
# board[2][0:4] = [7, 9, 12, 6]
#
backtrack(4)


# count_time(backtrack, 4)
