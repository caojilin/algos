import numpy as np

loots = {6: 30,
         3: 14,
         4: 16,
         2: 9}

W = 10


def knapspack_one(loots, W):
    table = np.zeros(W + 1)
    for i in range(1, W + 1):
        available = {}
        for w, v in loots.items():
            if w <= i:
                available[w] = v
        if available:
            candidates = []
            for key, value in available.items():
                candidates.append(table[i - key] + available[key])
            table[i] = max(candidates)
    return table


print(knapspack_one(loots, W))


def knapspack_two(loots, W):
    weights = [0] + list(loots.keys())
    values = [0] + list(loots.values())

    table = np.zeros((W + 1, len(loots) + 1))
    for i in range(1, W + 1):
        for j in range(1, len(loots) + 1):
            if weights[j] <= i:
                table[i][j] = max(table[i - weights[j]][j - 1] + values[j], table[i][j - 1])
            else:
                table[i][j] = table[i][j - 1]
    return table


print(knapspack_two(loots, W))
