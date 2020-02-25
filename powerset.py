n = 3


def power_set(arr):
    for i in range(8):
        j = list(reversed(bin(i)[2:]))
        if len(j) < n:
            j += ['0'] * (n - len(j))
        candidate = list(j)
        temp = []
        for k in range(n):
            if candidate[k] == '1':
                temp.append(arr[k])
        print(temp)


power_set('abc')
