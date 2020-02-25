import numpy as np

s1 = list("exponential")
s2 = list("polynomial")


def edit_distance(s1, s2):
    s1.insert(0, ' ')
    s2.insert(0, ' ')
    table = np.array([[0 for _ in range(len(s2))] for _ in range(len(s1))])

    for i in range(len(s1)):
        table[i][0] = i

    for j in range(1, len(s2)):
        table[0][j] = j

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            diff = 1 if s1[i] != s2[j] else 0
            table[i][j] = min(table[i - 1][j] + 1, table[i][j - 1] + 1, table[i - 1][j - 1] + diff)
    return table


print(edit_distance(s1, s2))
