from itertools import permutations
from time import time
from math import factorial

a = 0
b = 0


def brute_force(n):
    """
    list all possibilities
    :param n:
    :return:
    """

    def conflict(arr):
        """
        O(n^2)
        :param arr:
        :return:
        """
        if len(arr) > 1:
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if abs(arr[i] - arr[j]) in (0, j - i):
                        return True
        return False

    results = []
    for i in permutations(range(n)):
        if not conflict(i):
            results.append(i)
    return results


def run(n):
    time1 = time()

    final_queens = n_queen(n)
    # print(final_queens)
    print(len(final_queens))
    print(f"it takes {time() - time1:.2f} s")

    time1 = time()

    final_queens = brute_force(n)
    # print(final_queens)
    print(len(final_queens))
    print(f"it takes {time() - time1:.2f} s")


def n_queen(n):
    def conflict(queen_pos, cur_queen):
        """

        :param queen_pos: saved positions of queens, like [1,3]
        :param cur_queen: the position we are going to try, like pos=4
        :return: True if we can place new queen, False otherwise
        """
        arr_len = len(queen_pos)
        for index in range(arr_len):
            # if the distance between cur queen and any other queen is 0, it means two queens are on the same line
            # for example, queen_pos = [0,3], cur = 0
            # if the distance is the same as the difference between the indices, it means they are on the same diagonal
            # for example, queen_pos = [0,3], cur = 2
            # dis = 2 - 0 = 2, the difference of their indices is:
            # index of cur queen - index of 0:
            # which is equal to arr len - index(0) = 2 - 0 = 2
            if abs(cur_queen - queen_pos[index]) in (0, arr_len - index):
                return True
        return False

    def back(queen_pos=None):
        if queen_pos is None:
            queen_pos = []
        if len(queen_pos) == n:
            # remember to duplicate queen_pos, as it still points to
            final_result.append(queen_pos)
        else:
            for index in range(n):
                flag = conflict(queen_pos, index)
                if not flag:
                    back(queen_pos + [index])

    final_result = []
    back()
    return final_result


a = [1, 3, 0, 2]
n = len(a)
re = []
for i in a:
    re.append("." * i + "Q" + "." * (n - i-1))


def test(n):
    def conflict(queen_str, current_queen):
        n = len(queen_str)
        for i in range(n):
            if abs(current_queen - queen_str[i]) in (0, n - i):
                return True
        return False

    def back(queen_str=[]):
        if len(queen_str) == n:
            temp = []
            for i in queen_str:
                temp.append("." * i + "Q" + "." * (n - i - 1))
            results.append(temp)
        else:
            for i in range(n):
                flag = conflict(queen_str, i)
                if not flag:
                    back(queen_str + [i])

    results = []
    back()
    return results