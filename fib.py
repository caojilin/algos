import numpy as np
from math import sqrt
from time import time
from decimal import Decimal


def fib2(n):
    if n <= 1:
        return n
    f_pre, f_cur = 0, 1
    for i in range(1, n):
        temp = f_cur
        f_cur = f_pre + f_cur
        f_pre = temp
    return f_cur


def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib3(n):
    base = np.array([[0, 1], [1, 1]])

    right = np.array([[0], [1]])

    left = np.matmul(np.linalg.matrix_power(base, n), right)
    return left


def fib4(n):
    return Decimal(1) / Decimal(sqrt(5)) * ((Decimal(1) + Decimal(sqrt(5))) / 2) ** Decimal(n) - Decimal(1) / Decimal(
        sqrt(5)) * ((Decimal(1) - Decimal(sqrt(5))) / 2) ** Decimal(n)


def timing2(n, func):
    start = time()
    a = func(n)
    lapsed = time() - start
    print(f"it takes {lapsed} to calculate fib({n})")
    print(f"{a:.2e}")


funcs = [fib2, fib3, fib4]


def timing1(n):
    for i in funcs:
        timing2(n, i)


timing2(10*4, fib2)